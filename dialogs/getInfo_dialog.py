import logging
from pathlib import Path
import json
import pickle
import requests

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QThreadPool, QSize, Signal

from ui.get_info_dialog_ui import Ui_GetInfoDialog
from jobs.worker import Worker
from dialogs import showSuccessDialog, showFailDialog
from dialogs.login_dialog import LoginDialog
from globals import get_current_directory
from modules.Kordata.clients import get_clients
from modules.Kordata.sales import get_sales_notes, get_sales_invoices


class GetInfoDialog(QDialog):
    data_ready = Signal()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        logging.info("Inicializando GetInfoDialog")
        self.parent = parent
        self.ui = Ui_GetInfoDialog()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool.globalInstance()
        self.finished_count = 0
        self.errors = []

        self.sales = None
        self.invoices = None
        self.clients = None

        self.data_ready.connect(self.join_notes_and_items)
        self.data_ready.connect(lambda: self.ui.PlainTextLog.appendPlainText(
            "Unificando notas de venta e información de clientes..."
        ))

        self.get_all_data()

    def get_all_data(self):
        logging.info("Iniciando obtención de datos: notas, facturas y clientes")
        self.ui.PlainTextLog.appendPlainText(
            "Obteniendo notas de venta, facturas e información de clientes..."
        )
        self.finished_count = 0
        self.errors = []

        self.run_worker(get_sales_notes, self.set_salesNotes)
        self.run_worker(get_sales_invoices, self.set_invoices)
        self.run_worker(get_clients, self.set_clients)

    def run_worker(self, func, callback):
        logging.debug(f"Iniciando worker para: {func.__name__}")
        worker = Worker(func)
        worker.signals.result.connect(callback)
        worker.signals.onError.connect(self.handle_error)
        worker.signals.progress.connect(self.ui.PlainTextLog.appendPlainText)
        self.threadpool.start(worker)

    def set_salesNotes(self, sales):
        self.sales = sales
        logging.info(f"Notas de venta recibidas: {len(sales[0])} notas, {len(sales[1])} items")
        self.ui.PlainTextLog.appendPlainText(
            f"Notas de venta recibidas: {len(sales[0])} notas y {len(sales[1])} elementos"
        )
        self.check_all_finished()

    def set_invoices(self, invoices):
        self.invoices = invoices
        logging.info(f"Facturas recibidas: {len(invoices[0])} facturas, {len(invoices[1])} items")
        self.ui.PlainTextLog.appendPlainText(
            f"Facturas recibidas: {len(invoices[0])} facturas y {len(invoices[1])} elementos"
        )
        self.check_all_finished()

    def set_clients(self, clients):
        self.clients = clients
        logging.info(f"Clientes recibidos: {len(clients)}")
        self.ui.PlainTextLog.appendPlainText(
            f"Clientes recibidos: {len(clients)} clientes"
        )
        self.check_all_finished()
        if clients:
            self.transform_clients(clients)
        else:
            logging.log('No hay clientes')
        
    def transform_clients(self, clients):
        
        clients.pop(0)
        mapped_clients = {}
        for client in clients:
            mapped_clients[client["Nombre del cliente"]] = client
        try:
            dirname = Path(get_current_directory())
            clients_path = dirname / "clients.pkl"

            logging.debug(f"Guardando información en: {clients_path}")
            with open(clients_path, "wb") as f:
                pickle.dump(mapped_clients, f)

            showSuccessDialog(self, "Se actualizó la información correctamente")
            logging.info("Datos guardados exitosamente")
            

        except Exception as e:
            logging.exception("Error al guardar archivos")
            showFailDialog(
                self,
                "Ocurrió un error, revise que haya seleccionado los archivos correctos o que los exportó correctamente",
            )


    def check_all_finished(self):
        self.finished_count += 1
        logging.debug(f"Proceso terminado #{self.finished_count} de 3")
        if self.finished_count == 3:
            if self.errors:
                logging.error("Errores detectados al obtener datos: " + "; ".join(self.errors))
                QMessageBox.critical(
                    self, "Errores detectados", "\n\n".join(self.errors)
                )
                LoginDialog.launch(self.parent)
                self.close()
            else:
                logging.info("Todos los datos fueron obtenidos correctamente.")
                self.data_ready.emit()
            self.finished_count = 0

    def handle_error(self, message):
        logging.error(f"Error en worker: {message}")
        self.errors.append(message)
        self.check_all_finished()

    def join_notes_and_items(self):
        logging.info("Iniciando proceso de unión de datos")
        self.run_worker(self.process_data_merge, self.handle_merge_result)

    def process_data_merge(self, progress_callback, on_error, show_dialog):
        try:
            sales_notes, sales_notes_items = self.sales
            invoices, invoices_items = self.invoices
            clients = self.clients

            progress_callback.emit("Agregando elementos a las notas de venta y facturas...")
            logging.debug("Agregando elementos a documentos")

            def attach_items(data, items):
                for d in data:
                    d["items"] = [i for i in items if i["id"] == d["id"]]

            attach_items(sales_notes, sales_notes_items)
            attach_items(invoices, invoices_items)

            progress_callback.emit("Agregando teléfonos a las notas de venta y facturas...")
            logging.debug("Enlazando teléfonos de clientes")

            def attach_phone(data):
                for d in data:
                    phones = [
                        c["Teléfono"]
                        for c in clients
                        if c["Nombre del cliente"] == d["Cliente - Nombre del cliente"]
                    ]
                    d["phone"] = next(
                        (p for p in phones if p and isinstance(p, str)), None
                    )

            attach_phone(sales_notes)
            attach_phone(invoices)

            progress_callback.emit("Unificando notas de venta y facturas...")
            merged_data = invoices + sales_notes

            data_hash = {d["Folio"]: d for d in merged_data}
            logging.debug(f"Documentos totales unificados: {len(data_hash)}")

            progress_callback.emit("Convirtiendo datos a formato de búsqueda...")
            search_info = self.dictlist_to_str_list(
                merged_data,
                ["Folio", "Cliente - Nombre del cliente", "phone", "Fecha registro"],
            )

            return data_hash, search_info

        except Exception as e:
            error_msg = f"Error al unir notas y ventas: {e}"
            logging.exception(error_msg)
            progress_callback.emit(error_msg)
            raise RuntimeError(error_msg)

    def handle_merge_result(self, result):
        logging.info("Proceso de unión completado correctamente")
        data_hash, search_info = result
        self.save_info(data_hash=data_hash, search_info=search_info)

    def save_info(self, data_hash, search_info):
        try:
            dirname = Path(get_current_directory())
            sells_path = dirname / "sells.pkl"
            search_path = dirname / "search_data.pkl"

            logging.debug(f"Guardando información en: {sells_path} y {search_path}")
            with open(sells_path, "wb") as f:
                pickle.dump(data_hash, f)
            with open(search_path, "wb") as f:
                pickle.dump(search_info, f)

            showSuccessDialog(self, "Se actualizó la información correctamente")
            logging.info("Datos guardados exitosamente")
            self.parent.load_info()
            self.close()

        except Exception as e:
            logging.exception("Error al guardar archivos")
            showFailDialog(
                self,
                "Ocurrió un error, revise que haya seleccionado los archivos correctos o que los exportó correctamente",
            )

    def dictlist_to_str_list(self, lst, cols):
        logging.debug("Convirtiendo lista de dicts a lista de strings para búsqueda")
        result = []
        for row in lst:
            text = " - ".join(str(row.get(col, "")) for col in cols)
            text = text.replace("\n", "").replace("\r", "").strip()
            result.append(text)
        return result

    @staticmethod
    def launch(parent):
        logging.info("Lanzando GetInfoDialog desde launch()")
        dialog = GetInfoDialog(parent=parent)
        dialog.show()
