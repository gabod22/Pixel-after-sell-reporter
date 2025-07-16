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
import requests
import yaml
from os import path
from datetime import datetime, timedelta
from constants import config_file
from dialogs import showSuccessDialog, showFailDialog
from helpers import get_last_index, split_client_info, process_kor_table

from gspread_helpers import *
from modules.Google.contactsApi import get_credentials_people_api
from googleapiclient.discovery import build

from dotenv import load_dotenv

from globals import get_current_directory, getConfig

import pickle

from dialogs.login_dialog import LoginDialog
from dialogs.config_dialog import ConfigDialog
from dialogs.addContact_dialog import AddContactDialog
from dialogs.getInfo_dialog import GetInfoDialog


# from gspread import *

from modules.Trello.trelloConfig import trello_labels, trello_members
from modules.Trello.trelloApi import TrelloApi
from modules.Trello.trello_text_templates import (
    TRELLO_DESCRIPTION_TEMPLATE,
    TRELLO_CARD_NAME_TEMPLATE,
)

load_dotenv()
dirname = get_current_directory()

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

from modules.Kordata.auth import get_current_token


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
        self.ui.CbxType.addItems(trello_labels.keys())
        self._completing_client = False
        self._completing_sell_note = False

        self.ui.userInfoFrame.setVisible(False)

        self.config = getConfig()
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
        self.ui.CbxAgent.addItems(trello_members.keys())
        self.ui.CbxAgent.setCurrentText(self.config["TRELLO_DEFAULT_AGENT"])

        self.ui.actionActualizar_datos.triggered.connect(
            lambda: GetInfoDialog.launch(self)
        )
        self.ui.actionGuardar_contacto.triggered.connect(
            lambda: AddContactDialog.launch(self)
        )
        self.ui.actionConfiguracion.triggered.connect(lambda: ConfigDialog.launch(self))
        self.ui.accionLoginKordata.triggered.connect(lambda: LoginDialog.launch(self))
        self.clipboard = QGuiApplication.clipboard()

        self.assign_copy_buttons()

        try:
            credentials_path = path.join(dirname, "credentials.json")
            token_path = path.join(dirname, "token.json")
            self.creds_people = get_credentials_people_api(token_path, credentials_path)
        except:
            showFailDialog(
                self, "No se pudo obtener la información de inicio de sesión"
            )

    def assing_copy_functions(self):
        self.ui.BtnCopyBuyDate.connect()

    def copy_text(self, text):
        self.clipboard.setText(text)
        self.statusBar().showMessage(f"Se ha copiado al portapapeles {text}", 3000)

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
        self.ui.BtnCopyUser.clicked.connect(
            lambda: self.copy_text(self.ui.TxtUserName.text())
        )
        self.ui.BtnCopyUserPhone.clicked.connect(
            lambda: self.copy_text(self.ui.TxtUserPhone.text())
        )

        self.ui.BtnCopySeller.clicked.connect(
            lambda: self.copy_text(self.ui.TxtSeller.text())
        )

        self.ui.BtnCopyLeftDays.clicked.connect(
            lambda: self.copy_text(self.ui.LbLeftDays.text())
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
        sell_note, _, _, date = split_client_info(text)
        sell_note_data = self.sales_dict[sell_note]

        # date = sell_note_data["Fecha registro"]
        client_name = sell_note_data["Cliente - Nombre del cliente"]
        seller = sell_note_data["Vendedor"]

        self.ui.TxtUserName.setText(str(client_name))
        self.ui.TxtUserPhone.setText(str(sell_note_data["phone"]))
        self.ui.TxtClientName.setText(client_name)
        self.ui.TxtClientPhone.setText(str(sell_note_data["phone"]))
        self.ui.TxtNot.setText(str(sell_note))
        self.ui.TxtBuyDate.setText(date.strftime("%d/%m/%Y"))
        self.ui.TxtSeller.setText(str(seller))
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

        now = datetime.now().date()
        one_year = timedelta(days=365)

        left_days = date + one_year - now
        if int(left_days.days) < 0:
            self.ui.LbLeftDays.setText("Sin garantía")
        else:
            self.ui.LbLeftDays.setText(str(left_days.days))

        items = sell_note_data["items"]
        items_description = []
        for item in items:
            items_description.append(item["Descripcion"])
        if items == []:
            self.ui.TxtModel.setVisible(True)
            self.ui.CbxModel.setDisabled(True)
            self.ui.TxtModel.setFocus()
        else:
            self.ui.TxtModel.setVisible(False)
            self.ui.CbxModel.setDisabled(False)
            # self.ui.TxtModel.setFocus()
        self.ui.CbxModel.clear()
        self.ui.CbxModel.addItems(items_description)

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


        if not self.ui.CheckSameUser.isChecked():
            self.ui.TxtUserName.setText("")
            self.ui.TxtUserPhone.setText("")
            self.ui.TxtUserName.setEnabled(True)
            self.ui.TxtUserPhone.setEnabled(True)
            self.ui.userInfoFrame.setVisible(True)
        else:
            self.ui.TxtUserName.setEnabled(False)
            self.ui.TxtUserPhone.setEnabled(False)
            self.ui.userInfoFrame.setVisible(False)

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
        self.ui.LbLeftDays.setText("-")
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


    def load_info(self):
        print(
            path.join(dirname, "search_data.pkl"),
            path.isfile(path.join(dirname, "search_data.pkl")),
        )
        print(
            path.join(dirname, "sells.pkl"),
            path.isfile(path.join(dirname, "sells.pkl")),
        )
        if path.isfile(path.join(dirname, "search_data.pkl")) and path.isfile(
            path.join(dirname, "sells.pkl")
        ):
            with open(path.join(dirname, "search_data.pkl"), "rb") as file:
                self.simplied_sell_notes = pickle.load(file)
            with open(path.join(dirname, "sells.pkl"), "rb") as file:
                self.sales_dict = pickle.load(file)
                # print(self.sales_dict)

            self.completer_model.setStringList(self.simplied_sell_notes)
        else:
            showFailDialog(self, "No se pudo cargar la información de ventas")
            return {}, []

    def save_to_trello(self, info):
        trello = TrelloApi()
        self.statusBar().showMessage("Guardando en Trello")
        desc = TRELLO_DESCRIPTION_TEMPLATE.format(
            client_name=info["client_name"],
            client_phone=info["client_phone"],
            user_name=info["user_name"],
            user_phone=info["user_phone"],
            model=info["model"],
            issue=info["problem"],
            buy_date=info["buydate"],
            seller=info["seller"],
            left_days=info["left_days"],
        )
        card_name = TRELLO_CARD_NAME_TEMPLATE.format(
            phone=info["user_phone"], name=info["user_name"], buy_date=info["buydate"]
        )
        card_url = trello.add_card(
            cardName=card_name,
            desc=desc,
            labels=[info["type"]],
            members=[info["employee"]],
        )
        return card_url

    def save_to_google(self, info):
        self.statusBar().showMessage("Guardando el Google")

        sheet = get_worksheet()

        data = [
            [
                info["nota"],  ##Nota / factura
                info["user_name"],  ##Cliente
                info["user_phone"],  ##Contacto
                info["client_name"],  ##Nombre del cliente
                info["client_phone"],  ##Telefono del cliente
                info["buydate"],  ##Fecha de compra
                "",  ##Dias Restantes
                info["today"],  ##INICIO
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
                None,
                info["card_url"],  ##URL trello
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
        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = {
            "left_days": self.ui.LbLeftDays.text(),
            "user_name": self.ui.TxtUserName.text(),
            "user_phone": self.ui.TxtUserPhone.text(),
            "client_name": self.ui.TxtClientName.text(),
            "client_phone": self.ui.TxtClientPhone.text(),
            "today": today,
            "buydate": (
                self.ui.TxtSearch.text()
                if self.ui.CheckManualMode.isChecked()
                else date
            ),
            "nota": self.ui.TxtNot.text(),
            "model": self.ui.CbxModel.currentText(),
            "type": self.ui.CbxType.currentText(),
            "problem": self.ui.TxtProblem.toPlainText(),
            "employee": self.ui.CbxAgent.currentText(),
            "seller": self.ui.TxtSeller.text(),
        }
        self.statusBar().showMessage("Guardando registros...")
        trello_card_url = self.save_to_trello(data)
        data["card_url"] = trello_card_url
        self.statusBar().showMessage("Guardado en trello")
        
        
        self.save_to_google(data)
        self.statusBar().showMessage("Guardado en google sheets")
        
        # Registrar Cliente en Google Contacts
        if self.ui.CheckRegisterClient.isChecked():
            self.register_contact(name=data["client_name"], phone=data["client_phone"])
            self.statusBar().showMessage(f"Guardado {data["client_name"]} en Google Contacts")
            
        # Registrar Usuario en Google Contacts
        if self.ui.CheckSameUser.isChecked() and self.ui.CheckRegisterUser.isChecked():
            self.register_contact(name=data["user_name"], phone=data["user_phone"])
            self.statusBar().showMessage(f"Guardado {data["user_name"]} en Google Contacts")

        self.statusBar().showMessage("Registro guardado exitosamente", 4000)
        self.clear_inputs()
        showSuccessDialog(self, "Registrado correctamente")
        # except Exception as e:
        #     print("Error al registrar")

    def register_contact(self, name, phone):
        try:
            if not self.creds_people:
                self.creds_people = get_credentials_people_api(
                    path.join(dirname, "token.json"),
                    path.join(dirname, "credentials.json"),
                )
            service = build("people", "v1", credentials=self.creds_people)
            service.people().createContact(
                body={
                    "names": [{"givenName": name}],
                    "phoneNumbers": [{"value": phone}],
                }
            ).execute()
        except Exception as e:
            print("Error al registrar contacto en Google Contacts")
            print(e)
            showFailDialog(self, "No se pudo registrar el contacto en Google Contacts")
            return False
    def update_config(self):
        self.config = getConfig()
        self.ui.CbxAgent.clear()
        self.ui.CbxAgent.addItems(trello_members.keys())
        self.ui.CbxAgent.setCurrentText(self.config["TRELLO_DEFAULT_AGENT"])
        self.statusBar().showMessage("Configuración actualizada", 3000)

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
