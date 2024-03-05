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
        self.clients = self.get_clients_list()
        self.completer = QCompleter(self.clients)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setWidget(self.ui.TxtClientName)
        self.completer.activated.connect(self.handleCompletion)
        self.ui.TxtClientName.textChanged.connect(self.handleTextChanged)
        self.ui.BtnSave.clicked.connect(lambda: self.save_to_trello())
        self.ui.CheckSameUser.stateChanged.connect(self.handle_same_owner_change)
        self.ui.CheckSameUser.setChecked(True)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        self._completing = False

    def handle_select_client_change(self):
        _, client_name, client_phone = self.split_client_info(
            self.ui.TxtClientName.text()
        )
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

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
            f"{id} - {name} - {phone}".replace("\n", "").replace("\r", "")
            for id, name, phone in zip(
                clients_list[0],
                clients_list[1],
                clients_list[2],
            )
        ]
        return clients

    def get_sell_notes():
        pass

    def handleTextChanged(self, text):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        if not self._completing:
            found = False
            prefix = text.rpartition(",")[-1]
            if len(prefix) > 1:
                self.completer.setCompletionPrefix(prefix)
                if self.completer.currentRow() >= 0:
                    found = True
                    self.handle_select_client_change()
            if found:
                self.completer.complete()
            else:
                self.completer.popup().hide()

    def handleCompletion(self, text):
        if not self._completing:
            self._completing = True
            prefix = self.completer.completionPrefix()
            text = self.ui.TxtClientName.text()[: -len(prefix)] + text
            self.ui.TxtClientName.setText(text)
            _, client_name, client_phone = self.split_client_info(text)
            if self.ui.CheckSameUser.isChecked():
                self.ui.TxtUserName.setText(client_name)
                self.ui.TxtUserPhone.setText(client_phone)
                self.ui.TxtUserName.setEnabled(False)
                self.ui.TxtUserPhone.setEnabled(False)
            self._completing = False

    def split_client_info(self, str):
        client_info = str
        print(client_info)
        client_arr = client_info.replace(" - ", ",")
        client_arr = client_arr.split(",")
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
            Cliente: {1} - {2} 
            Usuario: {3} - {4}
            {5}
            {6}
            """.format(
                client_name, client_phone, user_name, user_phone, model, problem
            )
        else:
            desc = """
            Cliente: {1} - {2} 
            {3}
            {4}
            """.format(
                client_name, client_phone, model, problem
            )

        query = {
            "idList": "64e3a78386e39e4a09ee5dfa",
            "key": "2c0369eb0c76fbbbf4ecf3094fd31356",
            "token": "ATTA504126bdf847174a49735b9aae0a35f420aaf97820a22364aeda54ceeecc067cF815610B",
            "name": user_name + " " + nota,
            "desc": model + "\n" + problem,
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
