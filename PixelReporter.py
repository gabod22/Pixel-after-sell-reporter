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
from PySide6.QtGui import QGuiApplication

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
from google_contacts import get_credentials_people_api
from googleapiclient.discovery import build

from update_info_dialog import UpdateInfoDialog
from add_contact_dialog import AddContactDialog
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
    "Vendedor",
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
    "Reparación": "66db3f8a10ea602ee6292ec3",
    "Soporte": "66db3f8a10ea602ee6292eca",
}

members = {
    "GABRIEL": "64ece20aae1eb29dbbdeae66",
    "CENTRO SERVICIO": "613199d8efadf1307693adda",
    "CORAL": "6446fd35f1f734d3ec6183bd",
}

if getattr(sys, "frozen", False):
    dirname = path.dirname(sys.executable)
elif __file__:
    dirname = path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.creds_people = None
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
        self.creds_people = None

        self.sell_notes_items = {}
        self.sales_dict = {}
        self.simplied_sell_notes = []
        self.completer_model = QStringListModel()
        self.load_info()
        self.completer = QCompleter(self.completer_model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setWidget(self.ui.TxtSearch)
        self.completer.activated.connect(
            lambda text: self.handle_completion(
                text, self.ui.TxtSearch, self.completer, self._completing_client
            )
        )
        self.completer.highlighted.connect(
            lambda text: self.handle_select_client_change(text)
        )
        self.ui.TxtSearch.setCompleter(self.completer)
        self.ui.TxtSearch.textEdited.connect(self.handle_text_changed)
        self.ui.BtnSave.clicked.connect(lambda: self.save_report())
        self.ui.CheckSameUser.stateChanged.connect(self.handle_same_owner_change)
        self.ui.CheckSameUser.setChecked(True)
        self.ui.CheckManualMode.stateChanged.connect(self.handle_manual_mode_change)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        self.ui.CbxAgent.addItems(self.config["AGENTS"])

        self.ui.actionActualizar_datos.triggered.connect(self.show_update_info_dialog)
        self.ui.actionGuardar_contacto.triggered.connect(self.show_add_contact_dialog)
        self.clipboard = QGuiApplication.clipboard()
        self.assign_copy_buttons()
        
        try:
            self.creds_people = get_credentials_people_api()
        except:
            showFailDialog(self, "No se pudo obtener la información de inicio de sesión")
            
    def show_update_info_dialog(self):
        updateDialog = UpdateInfoDialog(parent=self)
        updateDialog.show()
        
    def show_add_contact_dialog(self):
        AddContact = AddContactDialog(parent=self)
        AddContact.show()

    def assing_copy_functions(self):
        self.ui.BtnCopyBuyDate.connect()

    def copy_text(self, text):
        self.clipboard.setText(text)
        self.statusBar().showMessage(f"Se ha copiado al portapapeles {text}",3000 )
        
        
    def assign_copy_buttons(self):
        self.ui.BtnCopyBuyDate.clicked.connect(
            lambda: self.copy_text(self.ui.TxtBuyDate.text())
        )

        self.ui.BtnCopyClientName.clicked.connect(
            lambda: self.copy_text(self.ui.TxtClientName.text())
        )

        self.ui.BtnCopyClientPhone.clicked.connect(
            lambda: self.copy_text(self.ui.TxtClientPhone.text())
        )

        self.ui.BtnCopySeller.clicked.connect(
            lambda: self.copy_text(self.ui.TxtSeller.text())
        )

        self.ui.BtnCopyLeftDays.clicked.connect(
            lambda: self.copy_text(self.ui.TxtLeftDays.text())
        )

        self.ui.BtnCopyModel.clicked.connect(
            lambda: self.copy_text(self.ui.CbxModel.currentText())
        )

        self.ui.BtnCopyNote.clicked.connect(
            lambda: self.copy_text(self.ui.TxtNot.text())
        )

    def handle_text_changed(self):
        self.clear_inputs()

    def handle_select_client_change(self, text):
        sell_note, _, _, _ = split_client_info(text)
        date = self.sales_dict[sell_note]["Fecha registro"]
        client_name = self.sales_dict[sell_note]["Nombre del cliente"]
        seller = self.sales_dict[sell_note]["Vendedor"]

        self.ui.TxtUserName.setText(str(client_name))
        self.ui.TxtUserPhone.setText(str(self.sales_dict[sell_note]["Teléfono"]))
        self.ui.TxtClientName.setText(client_name)
        self.ui.TxtClientPhone.setText(str(self.sales_dict[sell_note]["Teléfono"]))
        self.ui.TxtNot.setText(str(sell_note))
        self.ui.TxtBuyDate.setText(date.strftime("%d/%m/%Y"))
        self.ui.TxtSeller.setText(str(seller))
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

        now = datetime.now().date()
        one_year = timedelta(days=365)

        left_days = date.date() + one_year - now
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

    def handle_manual_mode_change(self):
        if self.ui.CheckManualMode.isChecked():
            self.ui.TxtSearch.setVisible(False)
            self.ui.CbxModel.setVisible(False)
            self.ui.TxtModel.setVisible(True)
        else:
            self.ui.TxtSearch.setVisible(True)
            self.ui.CbxModel.setVisible(True)
            self.ui.TxtModel.setVisible(False)

    def handle_same_owner_change(self):

        if self.ui.TxtSearch.text() != "":
            _, client_name, client_phone, date = split_client_info(
                self.ui.TxtSearch.text()
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

    def clear_inputs(self):
        self.ui.TxtUserName.setText("")
        self.ui.TxtUserPhone.setText("")
        self.ui.TxtLeftDays.setText("")
        self.ui.CbxModel.clear()
        self.ui.TxtNot.setText("")
        self.ui.TxtModel.setText("")
        self.ui.TxtBuyDate.setText("")
        self.ui.TxtClientName.setText("")
        self.ui.TxtClientPhone.setText("")
        self.ui.TxtSeller.setText("")
        self.ui.CbxModel.clear()
        self.ui.TxtProblem.setPlainText("")
        # self.ui.TxtSearch.setText("")

    def load_config(self):
        with open("config.yml", "r") as file:
            self.config = yaml.safe_load(file)

    def load_info(self):
        if path.isfile("sells.pkl") and path.isfile("sell_items.pkl"):
            with open("sells.pkl", "rb") as file:
                self.simplied_sell_notes = pickle.load(file)
            with open("sell_items.pkl", "rb") as file:
                self.sell_notes_items = pickle.load(file)
            with open("sales_dict.pkl", "rb") as file:
                self.sales_dict = pickle.load(file)
                # print(self.sales_dict)

            self.completer_model.setStringList(self.simplied_sell_notes)
        else:
            self.show_update_info_dialog()
            return {}, []

    def save_to_trello(self, info):


        if not self.ui.CheckSameUser.isChecked():
            desc = (
                "## Cliente \n nombre: {0} - {1} \n"
                "usuario: {2} - {3} \n"
                "### Modelo \n {4} \n"
                "### Problema \n {5} \n \n "
                "### Dirección \n [Dirección] \n"
                "### Información \n"
                "Fecha de compra: {6}  \n\n"
                "Vendedor: {7}"
                "Días restantes de garantía: {8}".format(
                    info["user_name"],
                    info["user_phone"],
                    info["user_name"],
                    info["user_phone"],
                    info["model"],
                    info["problem"],
                    info["buydate"],
                    info["seller"],
                    info["left_days"],
                )
            )
        else:
            desc = (
                "## Cliente \n "
                "nombre: {0} - {1} \n "
                "### Modelo \n {2} \n"
                "### Problema \n {3} \n"
                "### Dirección: \n [Dirección] \n"
                "### Información \n"
                "Fecha de compra: {4} \n "
                "Vendedor: {5} \n"
                "Días restantes de garantía: {6}".format(
                    info["user_name"], info["user_phone"], info["model"], info["problem"], info["buydate"], info["seller"], info["left_days"]
                )
            )

        query = {
            "idList": os.getenv("TRELLO_ID_LIST"),
            "key": os.getenv("TRELLO_KEY"),
            "token": os.getenv("TRELLO_TOKEN"),
            "name": info["user_phone"] + " - " + info["user_name"] + " - " + info["nota"],
            "desc": desc,
            "idLabels": [labels[info["type"]]],
            "idMembers": [members[info["employee"]]],
        }

        response = requests.request(
            "POST", trello_url, headers=trello_headers, params=query
        )
        # print(response.status_code,response.text)
        if response.status_code == 200:
            print("todo correcto")
            

        elif response.status_code == 401:
            showFailDialog(self, "Error, no se pudo agregar, no tiene los permisos.")

        else:
            showFailDialog(self, "Algo salió mal, contacta con el administrador")

    def save_to_google(self, info):
        self.statusBar().showMessage("Guardando el Google")
        

        sheet = get_worksheet()

        data = [
            [
                info["nota"],  ##Nota / factura
                info["user_name"],  ##Cliente
                info["user_phone"],  ##Contacto
                info["buydate"],  ##Fecha de compra
                "",  ##Dias Restantes
                info["hoy"],  ##INICIO
                "",  ##FIN
                True,  ##ACTIVO
                info["type"],
                info["employee"],
                info["seller"],  ##VENDEDOR
                "",  ##NUEVA NOTA /FACTURA
                info["model"],  ##MODELO DEL EQUIPO
                "",  ##NUMERO DE SERIE
                "",  ##ORDEN DE SERVICIO
                info["problem"],
                "",  ##Solucion brindada
                "",  ##Recursos, tiempo
                "",  ##Costos
                "",  # Envios,
            ]
        ]
        try:
            write_in_last_row(data, sheet)
        except Exception as e:
            print("No se puede guardar en google")
            print(e)
            showFailDialog(self, "Ocurrió un error al guardar en Google")
            self.statusBar().showMessage("Error al guardar en Google")

    def save_report(self):
        if not self.ui.CheckManualMode.isChecked():
            _, client_name, client_phone, date = split_client_info(
                self.ui.TxtSearch.text()
            )
            date = date.strftime("%d/%m/%Y")
        hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = {
            "left_days":self.ui.TxtLeftDays.text(),
            "user_name" : self.ui.TxtUserName.text(),
            "user_phone" : self.ui.TxtUserPhone.text(),
            "hoy": hoy,
            "buydate" : self.ui.TxtSearch.text() if self.ui.CheckManualMode.isChecked() else date,
            "nota" : self.ui.TxtNot.text(),
            "model" : self.ui.CbxModel.currentText(),
            "type" : self.ui.CbxType.currentText(),
            "problem" : self.ui.TxtProblem.toPlainText(),
            "employee" : self.ui.CbxAgent.currentText(),
            "seller" : self.ui.TxtSeller.text(),
        }
        self.statusBar().showMessage("Guardando registros...")
        self.save_to_trello(data)
        self.statusBar().showMessage("Guardado en trello")
        self.save_to_google(data)
        self.statusBar().showMessage("Guardado en google sheets")
        if self.ui.CheckRegisterContact.isChecked():
            self.register_contact(data)
            self.statusBar().showMessage("Guardado en Google Contacts")
            
        self.statusBar().showMessage("Registro guardado exitosamente",4000)
        self.clear_inputs()
        showSuccessDialog(self,"Registrado correctamente")
        # except Exception as e:
        #     print("Error al registrar")
            
    def register_contact(self, info):
        service = build("people", "v1", credentials=self.creds_people)
        service.people().createContact( body={
        "names": [
            {
                "givenName": info["user_name"]
            }
        ],
        "phoneNumbers": [
            {
                'value': info["user_phone"]
            }
        ],
    }).execute()
        

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
