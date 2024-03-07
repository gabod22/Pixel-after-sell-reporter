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

from constants import trello_url, trello_headers

# from gspread import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._completing_client = False
        self._completing_sell_note = False
        self.clients = self.get_clients_list()
        self.clients_notes = self.mix_sell_note_clients()
        self.completer = QCompleter(self.clients)
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
        _, client_name, client_phone = self.split_client_info(text)
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        print(self.clients_notes[client_name.strip()])
        self.note_completer = QCompleter(self.clients_notes[client_name.strip()])
        self.note_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.note_completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.note_completer.setWidget(self.ui.TxtNot)
        self.note_completer.activated.connect(
            lambda text: self.handleCompletion(
                text, self.ui.TxtNot, self.note_completer, self._completing_sell_note
            )
        )
        self.ui.TxtNot.setCompleter(self.note_completer)

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
        clients_df = pd.read_excel("Clientes.xlsx")
        clients_list = list(
            clients_df[["id", "Nombre del cliente", "Teléfono"]]
            .to_dict("list")
            .values()
        )

        clients = [
            f"{id} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
            for id, name, phone in zip(
                clients_list[0],
                clients_list[1],
                clients_list[2],
            )
        ]
        return clients

    def mix_sell_note_clients(self):
        clients_notes = {}
        sell_notes_df = pd.read_excel("Notasdeventa.xlsx")
        sell_notes_df[
            [
                "Folio",
                "Cliente - Nombre del cliente",
                "Importe del total",
                "Cliente - Teléfono",
            ]
        ]

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

    # def handleTextChanged(self, text):
    #     self.ui.TxtUserName.setText("")
    #     self.ui.TxtUserPhone.setText("")
    #     if not self._completing:
    #         found = False
    #         prefix = text.rpartition(",")[-1]
    #         if len(prefix) > 1:
    #             self.completer.setCompletionPrefix(prefix)
    #             if self.completer.currentRow() >= 0:
    #                 found = True
    #         if found:
    #             self.completer.complete()
    #         else:
    #             self.completer.popup().hide()

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

        if self.ui.CheckSameUser.isChecked():
            desc = """
            Cliente: {0} - {1} 
            Usuario: {2} - {3}
            {4}
            {5}
            """.format(
                client_name, client_phone, user_name, user_phone, model, problem
            )
        else:
            desc = """
            Cliente: {0} - {1} 
            {2}
            {3}
            """.format(
                client_name, client_phone, model, problem
            )

        query = {
            "idList": "64e3a78386e39e4a09ee5dfa",
            "key": "2c0369eb0c76fbbbf4ecf3094fd31356",
            "token": "ATTA504126bdf847174a49735b9aae0a35f420aaf97820a22364aeda54ceeecc067cF815610B",
            "name": user_name + " " + nota,
            "desc": desc,
        }

        response = requests.request(
            "POST", trello_url, headers=trello_headers, params=query
        )

        print(response)
        print(
            json.dumps(
                json.loads(response.text),
                sort_keys=True,
                indent=4,
                separators=(",", ": "),
            )
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec())
