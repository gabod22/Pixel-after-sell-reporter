from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QLineEdit,
    QApplication,
    QCompleter,
)
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt, QStringListModel
from PySide6.QtGui import QCloseEvent, QIcon, QPixmap


from ui.aftersalesui_ui import Ui_MainWindow

import sys
import pandas as pd
import requests
import json
import yaml
from os import path
from datetime import datetime, timedelta
from constants import trello_url, trello_headers
from dialogs import showSuccessDialog, showFailDialog
from helpers import get_last_index, split_client_info, process_kor_table

from gspread_helpers import *

from update_info_dialog import UpdateInfoDialog

import os
from dotenv import load_dotenv

import pickle

# from gspread import *

load_dotenv()
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

labels = {
    "Garantía": "66db3f8a10ea602ee6292ec5",
    "Consulta": "66db3f8a10ea602ee6292ec2",
    "Reparación":"66db3f8a10ea602ee6292ec3",
    "Soporte": "66db3f8a10ea602ee6292eca"
}

members = {
    "GABRIEL": "64ece20aae1eb29dbbdeae66",
    "CENTRO SERVICIO": "613199d8efadf1307693adda",
    "CORAL": "6446fd35f1f734d3ec6183bd"
}

if getattr(sys, 'frozen', False):
    dirname = path.dirname(sys.executable)
elif __file__:
    dirname = path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon = QIcon()
        icon.addFile(
            path.join(dirname, "icono.ico"),
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.ui.TxtModel.setVisible(False)
        self.ui.CbxType.addItems(labels.keys())
        self._completing_client = False
        self._completing_sell_note = False
        
        self.ui.userBox.setVisible(False)
        
        self.config = None
        self.load_config()

        self.sell_notes_items = {}
        self.simplied_sell_notes = []
        self.completer_model = QStringListModel()
        self.load_info()
        self.completer = QCompleter(self.completer_model, self)
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
        self.ui.CbxAgent.addItems(self.config['AGENTS'])

        self.ui.actionActualizar_datos.triggered.connect(self.show_update_info_dialog)

    def show_update_info_dialog(self):
        updateDialog = UpdateInfoDialog(parent=self)
        updateDialog.show()

    def handle_text_changed(self):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.TxtLeftDays.setText("")
        self.ui.CbxModel.clear()
        self.ui.TxtNot.setText("")
        self.ui.TxtModel.setText("")
        self.ui.TxtBuyDate.setText("")

    def handle_select_client_change(self, text):
        sell_note, client_name, client_phone, date = split_client_info(text)
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtNot.setText(sell_note)
        self.ui.TxtBuyDate.setText(date.strftime('%d/%m/%Y'))
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        
        now = datetime.now().date()
        one_year = timedelta(days=365)
        
        left_days =  date + one_year - now
        if int(left_days.days) < 0:
            self.ui.TxtLeftDays.setText("Sin garantía")
        else:
            self.ui.TxtLeftDays.setText(str(left_days.days))
        
        items = self.sell_notes_items[sell_note]
        if items == []:
            self.ui.TxtModel.setVisible(True)
            self.ui.CbxModel.setDisabled(True)
            self.ui.TxtModel.setFocus()
        else:
            self.ui.TxtModel.setVisible(False)
            self.ui.CbxModel.setDisabled(False)
            # self.ui.TxtModel.setFocus()
        self.ui.CbxModel.clear()
        self.ui.CbxModel.addItems(items)

    def handle_same_owner_change(self):
        
        if self.ui.TxtClientName.text() != "":
            _, client_name, client_phone, date = split_client_info(
                self.ui.TxtClientName.text()
            )

            if self.ui.CheckSameUser.isChecked():
                self.ui.TxtUserName.setText(client_name)
                self.ui.TxtUserPhone.setText(client_phone)
                self.ui.TxtUserName.setEnabled(False)
                self.ui.TxtUserPhone.setEnabled(False)
                self.ui.userBox.setVisible(False)
                return

        if not self.ui.CheckSameUser.isChecked():
            self.ui.TxtUserName.setText("")
            self.ui.TxtUserPhone.setText("")
            self.ui.TxtUserName.setEnabled(True)
            self.ui.TxtUserPhone.setEnabled(True)
            self.ui.userBox.setVisible(True)
        else:
            self.ui.TxtUserName.setEnabled(False)
            self.ui.TxtUserPhone.setEnabled(False)
            self.ui.userBox.setVisible(False)

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
        self.ui.TxtLeftDays.setText("")
        self.ui.TxtNot.setText("")
        self.ui.TxtProblem.setPlainText("")
        self.ui.TxtBuyDate.setText("")
        self.ui.CbxModel.clear()
    def load_config(self):
        with open('config.yml', 'r') as file:
            self.config = yaml.safe_load(file)
            
            
    def load_info(self):
        if path.isfile("sells.pkl") and path.isfile("sell_items.pkl"):
            with open("sells.pkl", "rb") as file:
                self.simplied_sell_notes = pickle.load(file)

            with open("sell_items.pkl", "rb") as file:
                self.sell_notes_items = pickle.load(file)

            self.completer_model.setStringList(self.simplied_sell_notes)
        else:
            self.show_update_info_dialog()
            return {}, []

    def save_to_trello(self):
        _, client_name, client_phone, date = split_client_info(
            self.ui.TxtClientName.text()
        )
        
        left_days = self.ui.TxtLeftDays.text()
        user_name = self.ui.TxtUserName.text()
        user_phone = self.ui.TxtUserPhone.text()
        nota = self.ui.TxtNot.text()
        model = self.ui.CbxModel.currentText()
        type = self.ui.CbxType.currentText()
        problem = self.ui.TxtProblem.toPlainText()
        employee = self.ui.CbxAgent.currentText()

        if not self.ui.CheckSameUser.isChecked():
            desc = "## Cliente \n nombre: {0} - {1} \n usuario: {2} - {3} \n ### Modelo \n {4} \n ### Problema \n {5} \n \n Fecha de compra: {6}  \n\n Días restantes de garantía: {7}".format(
                client_name, client_phone, user_name, user_phone, model, problem, date, left_days
            )
        else:
            desc = "## Cliente \n nombre: {0} - {1} \n ### Modelo \n {2} \n ### Problema \n {3} \n \n Fecha de compra: {4} \n\n Días restantes de garantía: {5}".format(
                client_name, client_phone, model, problem, date, left_days
            )

        query = {
            "idList": os.getenv('TRELLO_ID_LIST'),
            "key": os.getenv('TRELLO_KEY'),
            "token": os.getenv('TRELLO_TOKEN'),
            "name": client_phone + " - " + user_name + " - " + nota,
            "desc": desc,
            "idLabels": [
                labels[type]
            ],
            "idMembers": [
                members[employee]
            ]
        }

        response = requests.request(
            "POST", trello_url, headers=trello_headers, params=query
        )
        # print(response.status_code,response.text)
        if response.status_code == 200:
            showSuccessDialog(self, "Se agregó correctamente")
            print("todo correcto")
            self.save_to_google()
            self.clean_inputs()

        elif response.status_code == 401:
            showFailDialog(self, "Error, no se pudo agregar, no tiene los permisos.")

        else:
            showFailDialog(self, "Algo salió mal, contacta con el administrador")

    def save_to_google(self):
        _, client_name, client_phone, date = split_client_info(
            self.ui.TxtClientName.text()
        )
        hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        date= date.strftime("%d/%m/%Y")
        
        left_days = self.ui.TxtLeftDays.text()
        
        user_name = self.ui.TxtUserName.text()
        user_phone = self.ui.TxtUserPhone.text()
        
        nota = self.ui.TxtNot.text()
        model = self.ui.CbxModel.currentText()
        type = self.ui.CbxType.currentText()
        
        problem = self.ui.TxtProblem.toPlainText()
        
        employee = self.ui.CbxAgent.currentText()
        
        sheet = get_worksheet()
        
        data = [[
            nota,##Nota / factura
            user_name,##Cliente
            user_phone,##Contacto
            date,##Fecha de compra
            hoy,##INICIO
            "",##FIN
            True,##ACTIVO
            employee,
            "Aquí va el vendedor",##VENDEDOR
            "",##NUEVA NOTA /FACTURA
            model,##MODELO DEL EQUIPO
            "",##NUMERO DE SERIE
            "",##ORDEN DE SERVICIO
            problem,
            "",##Solucion brindada
            "",##Recursos, tiempo
            "",##Costos
            "",#Envios,
            type
        ]]
        write_in_last_row(data, sheet)

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
