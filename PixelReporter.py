from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QLineEdit,
    QApplication,
    QCompleter,
)
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt
from PySide6.QtGui import QCloseEvent, QIcon, QPixmap

from ui.aftersalesui_ui import Ui_MainWindow

import sys
import pandas as pd
import requests
import json
from os import path

from constants import trello_url, trello_headers
from dialogs import showSuccessDialog, showFailDialog
from helpers import get_last_index, split_client_info

# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))

sell_notes_columns = [
    "Folio",
    "Sucursal",
    "Nombre del cliente",
    "Fecha registro",
    "Estado",
    "Subtotal",
    "Descuento",
    "Impuestos",
    "Importe del total",
    "Ejecutivo",
    

]
items_cols = [
    "SKU",
    "Descripcion",
    "Cantidad",
    "Precio unitario",
    "Impuestos",
    "Porcentaje de descuento",
    "Subtotal",
    "Importe",
]




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.delailed_filepath = path.join(dirname, "notasdeventadetalladas.xlsx")
        self.simplied_filepath = path.join(dirname, "notasdeventasimplificada.xlsx")
        self.simplied_invoice_path = path.join(dirname, "Facturacion.xlsx")
        self._completing_client = False
        self._completing_sell_note = False
        self.sell_notes_items = self.substract_details_from_kor_table(self.delailed_filepath, sell_notes_columns, items_cols)
        self.simplied_sell_notes = self.mix_invoices_sellnotes()
        self.completer = QCompleter(self.simplied_sell_notes)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setWidget(self.ui.TxtClientName)
        self.completer.activated.connect(
            lambda text: self.handleCompletion(
                text, self.ui.TxtClientName, self.completer, self._completing_client
            )
        )
        self.completer.highlighted.connect(lambda text: self.handle_select_client_change(text))
        self.ui.TxtClientName.setCompleter(self.completer)
        self.ui.TxtClientName.textEdited.connect(self.handle_text_changed)
        self.ui.BtnSave.clicked.connect(lambda: self.save_to_trello())
        self.ui.CheckSameUser.stateChanged.connect(self.handle_same_owner_change)
        self.ui.CheckSameUser.setChecked(True)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

    def handle_text_changed(self):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.CbxModel.clear()

    def handle_select_client_change(self, text):
        sell_note, client_name, client_phone = split_client_info(text)
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtNot.setText(sell_note)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        items = self.sell_notes_items[sell_note]
        self.ui.CbxModel.addItems(items)

    def handle_same_owner_change(self):
        if self.ui.TxtClientName.text() != "":
            _, client_name, client_phone = split_client_info(
                self.ui.TxtClientName.text()
            )

            if self.ui.CheckSameUser.isChecked():
                self.ui.TxtUserName.setText(client_name)
                self.ui.TxtUserPhone.setText(client_phone)
                self.ui.TxtUserName.setEnabled(False)
                self.ui.TxtUserPhone.setEnabled(False)
                return
            
        if not self.ui.CheckSameUser.isChecked():    
            self.ui.TxtUserName.setText("")
            self.ui.TxtUserPhone.setText("")
            self.ui.TxtUserName.setEnabled(True)
            self.ui.TxtUserPhone.setEnabled(True)
        else:
            self.ui.TxtUserName.setEnabled(False)
            self.ui.TxtUserPhone.setEnabled(False)

    def get_clients_list(self):
        clients_df = pd.read_excel(path.join(dirname, "Clientes.xlsx"))
        clients_df = clients_df[["Nombre del cliente", "Teléfono"]]
        clients_df.drop_duplicates(subset=["Nombre del cliente"], inplace=True)
        
        return clients_df

    def mix_invoices_sellnotes(self):
        sell_notes = self.get_sell_notes(self.simplied_filepath)
        invoices = self.get_invoices(self.simplied_invoice_path)
        return sell_notes + invoices

    def df_to_list_str(self, df, headers:list):
        # simplified_table.rename(columns={"Cliente - Nombre del cliente": "Nombre del cliente", "Cliente - Teléfono": "Teléfono"}, inplace=True)
        sell_notes_list = list(
            df[
                [
                    "Folio",
                    "Nombre del cliente",
                    "Teléfono",
                ]
            ]
            .to_dict("list")
            .values()
        )
        sell_notes = [
            f"{folio} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
            for folio, name, phone in zip(
                sell_notes_list[0],
                sell_notes_list[1],
                sell_notes_list[2],
            )
        ]
        return sell_notes

    def get_invoices(self):
        invoices_df = pd.read_excel(path.join(dirname, "Facturacion.xlsx"))
        invoices_df.rename(
            columns={"Cliente - Nombre del cliente": "Nombre del cliente"}, inplace=True
        )
        clients = self.get_clients_list()
        invoices_df = invoices_df.merge(clients, on="Nombre del cliente", how="left")
        invoices_df_list = list(
            invoices_df[
                [
                    "Folio",
                    "Nombre del cliente",
                    "Importe total",
                    "Teléfono",
                ]
            ]
            .to_dict("list")
            .values()
        )
        sell_notes = [
            f"{folio} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
            for folio, name, phone in zip(
                invoices_df_list[0],
                invoices_df_list[1],
                invoices_df_list[3],
            )
        ]
        return sell_notes


    def handleCompletion(
        self, text, txt_line: QLineEdit, completer: QCompleter, completing
    ):
        if not completing:
            completing = True
            prefix = completer.completionPrefix()
            txt_line.setText(txt_line.text()[: -len(prefix)] + text)
            completing = False

    def clean_inputs(self):
        self.ui.TxtClientName.setText("")
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.CbxModel.clear()
        self.ui.TxtOS.setText("")
        self.ui.TxtNot.setText("")
        self.ui.TxtProblem.setPlainText("")

    def save_to_trello(self):
        _, client_name, client_phone = split_client_info(
            self.ui.TxtClientName.text()
        )
        user_name = self.ui.TxtUserName.text()
        user_phone = self.ui.TxtUserPhone.text()
        nota = self.ui.TxtNot.text()
        model = self.ui.CbxModel.currentText()
        os = self.ui.TxtOS.text()
        type = self.ui.CbxType.currentText()
        problem = self.ui.TxtProblem.toPlainText()

        if not self.ui.CheckSameUser.isChecked():
            desc = "## Cliente \n nombre: {0} - {1} \n usuario: {2} - {3} \n ### Modelo \n {4} \n ### Problema \n {5}".format(
                client_name, client_phone, user_name, user_phone, model, problem
            )
        else:
            desc = "## Cliente \n nombre: {0} - {1} \n ### Modelo \n {2} \n ### Problema \n {3}".format(
                client_name, client_phone, model, problem
            )

        query = {
            "idList": "65e78f80936ca9a151fa2de8",
            "key": "2c0369eb0c76fbbbf4ecf3094fd31356",
            "token": "ATTA3bb61958d5b3506b54860df6410561d10f408ed793e46cc60846737fac06cbc07E9CEBB9",
            "name": user_name + " - " + nota + " - " + type,
            "desc": desc,
            "idLabels": [
                "65e78f83936ca9a151fa59dd",
            ],
        }

        response = requests.request(
            "POST", trello_url, headers=trello_headers, params=query
        )
        # print(response.status_code,response.text)
        if response.status_code == 200:
            showSuccessDialog(self, "Se agregó correctamente")
            print("todo correcto")
            self.clean_inputs()

        elif response.status_code == 401:
            showFailDialog(self, "Error, no se pudo agregar, no tiene los permisos.")

        else:
            showFailDialog(self, "Algo salió mal, contacta con el administrador")
    
    # def clean_sell_notes(self, filepath):
    #     try:
    #         detailed_sell_notes = pd.read_excel(filepath)
    #     except Exception as e:
    #         raise "No se pudo abrir el documento:" + e

        
    #     detailed_sell_notes.drop(detailed_sell_notes.index[0:7], inplace=True)
    #     detailed_sell_notes.reset_index(drop=True, inplace=True)
    #     # detailed_sell_notes.set_axis(sell_notes_columns, axis=1)
        
        
    #     return detailed_sell_notes.set_axis(sell_notes_columns, axis=1)
    
    def substract_details_from_kor_table(self, detailed_filepath, header, items_header):
        id_items = {}
        try:
            detailed_table = pd.read_excel(detailed_filepath)
        except Exception as e:
            raise "No se pudo abrir el documento:" + e

        
        detailed_table.drop(detailed_table.index[0:7], inplace=True)
        detailed_table = detailed_table.reset_index(drop=True)
        detailed_table = detailed_table.set_axis(header, axis=1)
        simplified_table = detailed_table.dropna(
            subset=['Folio'], inplace=False
        )
        last_index = get_last_index(detailed_table)
        table_indexs  = simplified_table.index.append(
            pd.Index([last_index])
        )
        
            
        for inx in range(len(table_indexs) - 1):
            items_df = pd.DataFrame(
                detailed_table.iloc[
                    table_indexs[inx] + 2 : table_indexs[inx + 1] - 1,
                    [1, 2, 3, 4, 5, 6, 7, 8],
                ]
            )
            # print(items_df)
            items_df.columns = items_header
            sell_notes_list = list(
                items_df[
                    [
                        "SKU",
                        "Descripcion"
                    ]
                ]
                .to_dict("list")
                .values()
            )
            items = [
                f"{sku} - {description}".replace("\n", "").replace("\r", "").strip()
                for sku, description in zip(
                    sell_notes_list[0],
                    sell_notes_list[1],
                )
            ]
            # print(sell_notes_list)
            id = simplified_table.iloc[inx,0]
            
            id_items[id] = items
        return id_items
    
    def save_excel(self, df: pd.DataFrame, book_name: str, sheet_name: str):
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(book_name + ".xlsx", engine="xlsxwriter")
        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        # Add a format.
        text_format = workbook.add_format({"text_wrap": True})
        # Resize columns for clarity and add formatting to column C.
        worksheet.set_column(4, 4, 70, text_format)
        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

        


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec())




    # def mix_sell_note_clients(self):
    #     clients_notes = {}
    #     try:
    #         sell_notes_df = pd.read_excel("Notasdeventa.xlsx")
    #         sell_notes_df[
    #             [
    #                 "Folio",
    #                 "Nombre del cliente",
    #                 "Importe del total",
    #                 "Cliente - Teléfono",
    #             ]
    #         ]
    #     except Exception as e:
    #         showFailDialog(
    #             self,
    #             "No se pudo abrir el documento de las notas de venta, revise que el archivo exista o no esté dañado.",
    #         )
    #         return []

    #     for inx in sell_notes_df.index:
    #         clients_notes[sell_notes_df["Cliente - Nombre del cliente"].iloc[inx]] = []

    #     for inx in sell_notes_df.index:
    #         clients_notes[
    #             sell_notes_df["Cliente - Nombre del cliente"].iloc[inx]
    #         ].append(
    #             "{0} - {1} - {2}".format(
    #                 sell_notes_df["Folio"].iloc[inx],
    #                 round(sell_notes_df["Importe del total"].iloc[inx], 2),
    #                 sell_notes_df["Fecha registro"].iloc[inx],
    #             ),
    #         )

    #     return clients_notes