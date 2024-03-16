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

# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._completing_client = False
        self._completing_sell_note = False
        # self.clients = self.get_clients_list()
        # self.clients_notes = self.mix_sell_note_clients()
        self.sell_notes = self.mix_invoices_sellnotes()
        self.completer = QCompleter(self.sell_notes)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setWidget(self.ui.TxtClientName)
        self.completer.activated.connect(
            lambda text: self.handleCompletion(
                text, self.ui.TxtClientName, self.completer, self._completing_client
            )
        )
        self.completer.highlighted.connect(self.handle_select_client_change)
        self.ui.TxtClientName.setCompleter(self.completer)
        self.ui.TxtClientName.textEdited.connect(self.text_changed)
        self.ui.BtnSave.clicked.connect(lambda: self.save_to_trello())
        self.ui.CheckSameUser.stateChanged.connect(self.handle_same_owner_change)
        self.ui.CheckSameUser.setChecked(True)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

    def text_changed(self):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")

    def handle_select_client_change(self, text):
        sell_note, client_name, client_phone = self.split_client_info(text)
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtNot.setText(sell_note)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        # print(self.clients_notes[client_name.strip()])
        # self.note_completer = QCompleter(self.clients_notes[client_name.strip()])
        # self.note_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # self.note_completer.setFilterMode(Qt.MatchFlag.MatchContains)
        # self.note_completer.setWidget(self.ui.TxtNot)
        # self.note_completer.activated.connect(
        #     lambda text: self.handleCompletion(
        #         text, self.ui.TxtNot, self.note_completer, self._completing_sell_note
        #     )
        # )
        # self.ui.TxtNot.setCompleter(self.note_completer)

    def handle_same_owner_change(self):
        _, client_name, client_phone = self.split_client_info(
            self.ui.TxtClientName.text()
        )

        if self.ui.CheckSameUser.isChecked():
            self.ui.TxtUserName.setText(client_name)
            self.ui.TxtUserPhone.setText(client_phone)
            self.ui.TxtUserName.setEnabled(False)
            self.ui.TxtUserPhone.setEnabled(False)
            return
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.TxtUserName.setEnabled(True)
        self.ui.TxtUserPhone.setEnabled(True)
        return

    def get_clients_list(self):
        clients_df = pd.read_excel(path.join(dirname, "Clientes.xlsx"))
        clients_df = clients_df[["Nombre del cliente", "Teléfono"]]
        # clients_list = list(
        #     clients_df[["id", "Nombre del cliente", "Teléfono"]]
        #     .to_dict("list")
        #     .values()
        # )

        # clients = [
        #     f"{id} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
        #     for id, name, phone in zip(
        #         clients_list[0],
        #         clients_list[1],
        #         clients_list[2],
        #     )
        # ]
        return clients_df
    
    def mix_invoices_sellnotes(self):
        sell_notes = self.get_sell_notes()
        invoices = self.get_invoices()
        return sell_notes + invoices

    def get_sell_notes(self):
        sell_notes_df = pd.read_excel(path.join(dirname, "Notasdeventa.xlsx"))
        sell_notes_df.rename(columns={"Cliente - Nombre del cliente": "Nombre del cliente", "Cliente - Teléfono": "Teléfono"}, inplace=True)
        sell_notes_list = list(
            sell_notes_df[
                [
                    "Folio",
                    "Nombre del cliente",
                    "Importe del total",
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
                sell_notes_list[3],
            )
        ]
        return sell_notes
    
    def get_invoices(self):
        invoices_df = pd.read_excel(path.join(dirname, "Facturacion.xlsx"))
        invoices_df.rename(columns={"Cliente - Nombre del cliente": "Nombre del cliente"}, inplace=True)
        clients = self.get_clients_list()
        invoices_df = invoices_df.merge(clients, on= "Nombre del cliente", how="left")
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

    def mix_sell_note_clients(self):
        clients_notes = {}
        try:
            sell_notes_df = pd.read_excel("Notasdeventa.xlsx")
            sell_notes_df[
            [
                "Folio",
                "Nombre del cliente",
                "Importe del total",
                "Cliente - Teléfono",
            ]
        ]
        except Exception as e:
            showFailDialog(self, "No se pudo abrir el documento de las notas de venta, revise que el archivo exista o no esté dañado.")
            return []

        for inx in sell_notes_df.index:
            clients_notes[sell_notes_df["Cliente - Nombre del cliente"].iloc[inx]] = []

        for inx in sell_notes_df.index:
            clients_notes[
                sell_notes_df["Cliente - Nombre del cliente"].iloc[inx]
            ].append(
                "{0} - {1} - {2}".format(
                    sell_notes_df["Folio"].iloc[inx],
                    round(sell_notes_df["Importe del total"].iloc[inx], 2),
                    sell_notes_df["Fecha registro"].iloc[inx],
                ),
            )

        return clients_notes

    def handleCompletion(
        self, text, txt_line: QLineEdit, completer: QCompleter, completing
    ):
        if not completing:
            completing = True
            prefix = completer.completionPrefix()
            txt_line.setText(txt_line.text()[: -len(prefix)] + text)

            completing = False

    def split_client_info(self, str):
        print(str)
        client_arr = str.split(" - ")
        client_id = client_arr[0]
        client_name = client_arr[1]
        client_phone = client_arr[2]
        return client_id, client_name, client_phone

    def clean_inputs(self):
        self.ui.TxtClientName.setText("")
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.TxtModel.setText("")
        self.ui.TxtOS.setText("")
        self.ui.TxtNot.setText("")
        self.ui.TxtProblem.setPlainText("")
    def save_to_trello(self):
        _, client_name, client_phone = self.split_client_info(
            self.ui.TxtClientName.text()
        )
        user_name = self.ui.TxtUserName.text()
        user_phone = self.ui.TxtUserPhone.text()
        nota = self.ui.TxtNot.text()
        model = self.ui.TxtModel.text()
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
        if(response.status_code == 200):
            showSuccessDialog(self, "Se agregó correctamente")
            print("todo correcto")
            self.clean_inputs()
            
        elif(response.status_code == 401):
            showFailDialog(self, "Error, no se pudo agregar, no tiene los permisos.")
        
        else:
            showFailDialog(self, "Algo salió mal, contacta con el administrador")



if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec())
