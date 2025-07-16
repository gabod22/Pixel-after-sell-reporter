from PySide6.QtWidgets import (
    QDialog,
)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt, Signal
from ui.get_info_dialog_ui import Ui_GetInfoDialog

# from tabulate import tabulate

from jobs.worker import Worker
from os import path

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
from dialogs.login_dialog import LoginDialog

import requests
import json
import pickle

from globals import get_current_directory
from modules.Kordata.clients import get_clients
from modules.Kordata.sales import get_sales_notes, get_sales_invoices

dirname = get_current_directory()


class GetInfoDialog(QDialog):
    data_ready = Signal()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
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
        self.data_ready.connect(
            lambda: self.ui.PlainTextLog.appendPlainText(
                "Unificando notas de venta e información de clientes..."
            )
        )
        self.get_all_data()

    def thread_get_sales_notes(self):
        worker = Worker(get_sales_notes)
        worker.signals.result.connect(self.set_salesNotes)
        # worker.signals.finished.connect(self.DiskInfoDone)
        worker.signals.onError.connect(self.handle_error)
        worker.signals.progress.connect(self.ui.PlainTextLog.appendPlainText)
        self.threadpool.start(worker)

    def thread_get_sales_invoices(self):
        worker = Worker(get_sales_invoices)
        worker.signals.result.connect(self.set_invoices)
        # worker.signals.finished.connect(self.DiskInfoDone)
        worker.signals.onError.connect(self.handle_error)
        worker.signals.progress.connect(self.ui.PlainTextLog.appendPlainText)
        self.threadpool.start(worker)

    def thread_get_clients(self):
        worker = Worker(get_clients)
        worker.signals.result.connect(self.set_clients)
        # worker.signals.finished.connect(self.DiskInfoDone)
        worker.signals.onError.connect(self.handle_error)
        worker.signals.progress.connect(self.ui.PlainTextLog.appendPlainText)
        self.threadpool.start(worker)

    def set_salesNotes(self, sales):
        self.sales = sales
        self.ui.PlainTextLog.appendPlainText(
            f"Notas de venta recibidas: {len(sales[0])} notas y {len(sales[1])} elementos"
        )
        self.check_all_finished()

    def set_invoices(self, invoices):
        self.invoices = invoices
        self.ui.PlainTextLog.appendPlainText(
            f"Facturas recibidas: {len(invoices[0])} facturas y {len(invoices[1])} elementos"
        )
        self.check_all_finished()

    def set_clients(self, clients):
        self.clients = clients
        self.ui.PlainTextLog.appendPlainText(
            f"Clientes recibidos: {len(clients)} clientes"
        )
        self.check_all_finished()

    def check_all_finished(self):
        self.finished_count += 1
        print(f"Finished count: {self.finished_count}")

        if self.finished_count == 3:
            if self.errors:
                error_msg = "\n\n".join(self.errors)
                QMessageBox.critical(
                    self,
                    "Errores detectados",
                    f"Ocurrieron los siguientes errores:\n\n{error_msg}",
                )
                LoginDialog.launch(self.parent)
                self.close()
            else:
                print("Todos los threads terminaron correctamente")
                self.data_ready.emit()

    def get_all_data(self):
        self.ui.PlainTextLog.appendPlainText(
            "Obteniendo notas de venta, facturas e información de clientes..."
        )
        self.finished_count = 0
        self.errors = []

        self.thread_get_sales_notes()
        self.thread_get_sales_invoices()
        self.thread_get_clients()

    def handle_error(self, message):
        self.errors.append(message)
        self.check_all_finished()

    def join_notes_and_items(self):
        self.ui.PlainTextLog.appendPlainText(
            "Unificando notas de venta e información de clientes..."
        )
        sales_notes, sales_notes_items = self.sales
        invoices, invoices_items = self.invoices
        clients = self.clients
        # print(clients)

        for note in sales_notes:
            # Filtrar elementos de array2 que coincidan en id
            note["items"] = [
                sub_item
                for sub_item in sales_notes_items
                if sub_item["id"] == note["id"]
            ]

        for note in sales_notes:
            phones = [
                client["Teléfono"]
                for client in clients
                if client["Nombre del cliente"] == note["Cliente - Nombre del cliente"]
            ]
            phone_r = None
            if phones:
                for phone in phones:
                    if phone != "" and type(phone) == str:
                        phone_r = phone
                        break
            note["phone"] = phone_r

        for invoice in invoices:
            # Filtrar elementos de array2 que coincidan en id
            invoice["items"] = [
                sub_item
                for sub_item in invoices_items
                if sub_item["id"] == invoice["id"]
            ]

        for invoice in invoices:
            phones = [
                client["Teléfono"]
                for client in clients
                if client["Nombre del cliente"]
                == invoice["Cliente - Nombre del cliente"]
            ]
            phone_r = None
            if phones:
                for phone in phones:
                    if phone != "" and type(phone) == str:
                        phone_r = phone
                        break
            invoice["phone"] = phone_r

        data = invoices + sales_notes

        search_info = self.dictlist_to_str_list(
            data, ["Folio", "Cliente - Nombre del cliente", "phone", "Fecha registro"]
        )
        # print(data)
        data_hash = {}

        for d in data:
            data_hash[d["Folio"]] = d

        json_object = json.dumps(data_hash, indent=4)

        self.save_info(data_hash, search_info)

    def save_info(self, data_hash, array):
        try:

            with open(path.join(dirname, "sells.pkl"), "wb") as file:
                pickle.dump(data_hash, file)
            with open(path.join(dirname, "search_data.pkl"), "wb") as file:
                pickle.dump(array, file)

            showSuccessDialog(self, "Se actualizó la información correctamente")
            self.parent.load_info()
            self.close()

        except Exception as e:
            showFailDialog(
                self,
                "Ocurrió un error, revise que haya seleccionado los archivos correctos o que los exportó correctamente",
            )
            print(e)

    def update_info(self):
        pass

    def dictlist_to_str_list(self, list, cols):
        result = []
        for row in list:
            text = ""
            for i, col in enumerate(cols):
                value = row[col] if row[col] != None else ""
                text = text + str(value)

                if i < len(cols) - 1:
                    text = text + " - "
            text = text.replace("\n", "").replace("\r", "").strip()
            result.append(text)
        return result

    @staticmethod
    def launch(parent):
        dialog = GetInfoDialog(parent=parent)
        dialog.show()
