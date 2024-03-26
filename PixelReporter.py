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
from helpers import get_last_index, split_client_info, process_kor_table

from update_info_dialog import UpdateInfoDialog


import pickle

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
        icon = QIcon()
        icon.addFile(
            path.join(path.dirname(__file__), "icono.ico"),
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.ui.TxtModel.setVisible(False)
        
        self._completing_client = False
        self._completing_sell_note = False

        self.sell_notes_items, self.simplied_sell_notes = self.load_info()

        self.completer = QCompleter(self.simplied_sell_notes)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setWidget(self.ui.TxtClientName)
        self.completer.activated.connect(
            lambda text: self.handle_completion(
                text, self.ui.TxtClientName, self.completer, self._completing_client
            )
        )
        self.completer.highlighted.connect(
            lambda text: self.handle_select_client_change(text)
        )
        self.ui.TxtClientName.setCompleter(self.completer)
        self.ui.TxtClientName.textEdited.connect(self.handle_text_changed)
        self.ui.BtnSave.clicked.connect(lambda: self.save_to_trello())
        self.ui.CheckSameUser.stateChanged.connect(self.handle_same_owner_change)
        self.ui.CheckSameUser.setChecked(True)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

        self.ui.actionActualizar_datos.triggered.connect(self.show_update_info_dialog)

    def show_update_info_dialog(self):
        updateDialog = UpdateInfoDialog(parent=self)
        updateDialog.show()

    def handle_text_changed(self):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.CbxModel.clear()
        self.ui.TxtNot.setText("")
        self.ui.TxtModel.setText("")

    def handle_select_client_change(self, text):
        sell_note, client_name, client_phone = split_client_info(text)
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtNot.setText(sell_note)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        try:
            items = self.sell_notes_items[sell_note]
        except:
            items = []
            self.ui.TxtModel.setVisible(True)
            self.ui.CbxModel.setDisabled(True)
            self.ui.TxtModel.setFocus()
        self.ui.CbxModel.clear()
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

    def handle_completion(
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
        self.ui.TxtOS.setText("")
        self.ui.TxtNot.setText("")
        self.ui.TxtProblem.setPlainText("")
        self.ui.CbxModel.clear()

    def load_info(self):
        if path.isfile('sells.pkl') and path.isfile('sell_items.pkl'):
            with open('sells.pkl', 'rb') as file:
                sells = pickle.load(file)
                
            with open('sell_items.pkl', 'rb') as file:
                sell_items = pickle.load(file)
            return sell_items, sells
        else:
            self.show_update_info_dialog()
            return {}, []
    def save_to_trello(self):
        _, client_name, client_phone = split_client_info(self.ui.TxtClientName.text())
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
