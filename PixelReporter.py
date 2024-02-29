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
from gspread import *


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
        self.ui.BtnSave.clicked.connect(lambda: self.save_record())
        self._completing = False

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

    def handleTextChanged(self, text):
        if not self._completing:
            found = False
            prefix = text.rpartition(",")[-1]
            if len(prefix) > 1:
                self.completer.setCompletionPrefix(prefix)
                if self.completer.currentRow() >= 0:
                    found = True
            if found:
                self.completer.complete()
            else:
                self.completer.popup().hide()

    def handleCompletion(self, text):
        if not self._completing:
            self._completing = True
            prefix = self.completer.completionPrefix()
            self.ui.TxtClientName.setText(
                self.ui.TxtClientName.text()[: -len(prefix)] + text
            )
            self._completing = False

    # def save_to_google(self):
    #     try:
    #         # progress_callback.emit('Obteniendo worksheet')
    #         wks = get_worksheet()
    #         print(wks)
    #     except Exception as e:

    #         # progress_callback.emit('Error al obtener el worksheet')
    #         print(e)
    #         return "No se guardó"

    #     try:
    #         # progress_callback.emit('Guardando...')
    #         write_r
    #         ange(
    #             self.data,
    #             self.notes,
    #             wks,
    #         )
    #         print("La info fue guardada correctamente")
    #     except Exception as e:
    #         # self.showFailDialog('La información no fue guardada.')
    #         # progress_callback.emit('No se guardó...')
    #         print("La info no fue guardad :C %s" % e)
    #         print(e)
    #     finally:
    #         self.data = [[]]
    #         self.notes = []

    #         return "Finalizado"

    def save_to_trello(self):
        client_name = self.ui.TxtClientName.text()
        client_arr = client_name.replace(" ", "")
        client_arr = client_arr.split("-")
        user_name = self.ui.TxtUserName.text()
        user_phone = self.ui.TxtUserPhone.text()
        nota = self.ui.TxtNot.text()
        model = self.ui.TxtModel.text()
        os = self.ui.TxtOS.text()
        type = self.ui.CbxType.currentText()
        problem = self.ui.TxtProblem.toPlainText()

        query = {
            "idList": "64e3a78386e39e4a09ee5dfa",
            "key": "2c0369eb0c76fbbbf4ecf3094fd31356",
            "token": "ATTA504126bdf847174a49735b9aae0a35f420aaf97820a22364aeda54ceeecc067cF815610B",
            "name": client_arr[1] + " " + nota,
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
