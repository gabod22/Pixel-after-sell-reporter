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
from pathlib import Path
from datetime import datetime, timedelta
import logging

from dialogs import showSuccessDialog, showFailDialog
from helpers import get_last_index, split_client_info, process_kor_table

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

from modules.Google.contactsApi import GoogleContactsApi
from modules.Google.sheetsApi import GoogleSpreadsheetApi


load_dotenv()
dirname = get_current_directory()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        icon_path = Path(dirname) / "assets/icono.ico"
        icon = QIcon()
        icon.addFile(
            str(icon_path),
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.setWindowIcon(icon)
        
        log_path = Path(dirname) / "app.log"
        logging.basicConfig(
            filename=str(log_path),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        
        self._completing_client = False
        self._completing_sell_note = False
        self.sell_notes_items = {}
        self.sales_dict = {}
        self.simplied_sell_notes = []


        self.completer = self.set_autocomplete()
        self.ui.TxtSearch.setCompleter(self.completer)
        self.config = getConfig()

        self.clipboard = QGuiApplication.clipboard()
        self.setup_init_state()
        self.setup_connections()
        self.load_info()
        try:
            credentials_path = Path(dirname) / "credentials.json"
            token_path =Path(dirname) / "token.json"
            self.googleContacts = GoogleContactsApi(str(token_path), str(credentials_path))
        except:
            showFailDialog(
                self, "No se pudo obtener la información de inicio de sesión"
            )
            
        google_api = GoogleSpreadsheetApi()
        google_api.get_email()
        try:
            worksheet = google_api.get_worksheet()
        except Exception as e:
            worksheet = None
            showFailDialog(self,str(e))
            "☑️ Error al guardar en google"
        print(worksheet)
        
        
            
    def setup_init_state(self):
        
        self.ui.TxtModel.setVisible(False)
        self.ui.userInfoFrame.setVisible(False)
        self.ui.CbxType.addItems(trello_labels.keys())
        self.ui.CheckSameUser.setChecked(True)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)
        self.ui.CbxAgent.addItems(trello_members.keys())
        self.ui.CbxAgent.setCurrentText(self.config["TRELLO_DEFAULT_AGENT"])
        
    def setup_connections(self):
        # Conexiones de botones para copiar texto
        copy_map = [
            (self.ui.BtnCopyBuyDate, self.ui.TxtBuyDate.text),
            (self.ui.BtnCopyClientName, self.ui.TxtClientName.text),
            (self.ui.BtnCopyClientPhone, self.ui.TxtClientPhone.text),
            (self.ui.BtnCopyUser, self.ui.TxtUserName.text),
            (self.ui.BtnCopyUserPhone, self.ui.TxtUserPhone.text),
            (self.ui.BtnCopySeller, self.ui.TxtSeller.text),
            (self.ui.BtnCopyLeftDays, self.ui.LbLeftDays.text),
            (self.ui.BtnCopyModel, self.ui.CbxModel.currentText),
            (self.ui.BtnCopyNote, self.ui.TxtNot.text),
        ]

        for button, get_text in copy_map:
            button.clicked.connect(lambda _, g=get_text: self.copy_text(g()))

        # Conexiones de señales generales
        signals = [
            (self.ui.TxtSearch.textEdited, self.clear_inputs),
            (self.ui.CheckSameUser.stateChanged, self.handle_same_owner_change),
            (self.ui.CheckManualMode.stateChanged, self.handle_manual_mode_change),
            (self.ui.BtnSave.clicked, lambda: self.save_report()),
        ]
        for signal, slot in signals:
            signal.connect(slot)

        # Conexiones del menú
        menu_actions = [
            (self.ui.actionActualizar_datos.triggered, lambda: GetInfoDialog.launch(self)),
            (self.ui.actionGuardar_contacto.triggered, lambda: AddContactDialog.launch(self)),
            (self.ui.actionConfiguracion.triggered, lambda: ConfigDialog.launch(self)),
            (self.ui.accionLoginKordata.triggered, lambda: LoginDialog.launch(self)),
        ]
        for action, func in menu_actions:
            action.connect(func)
            
        connections = [
            (self.ui.TxtSearch.textEdited, self.clear_inputs),
            (self.ui.CheckSameUser.stateChanged, self.handle_same_owner_change),
            (self.ui.CheckManualMode.stateChanged, self.handle_manual_mode_change),
            (self.ui.BtnSave.clicked, lambda: self.save_report()),
        ]

        for signal, slot in connections:
            signal.connect(slot)

    def set_autocomplete(self):
        self.completer_model = QStringListModel()
        completer = QCompleter(self.completer_model, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setWidget(self.ui.TxtSearch)
        completer.activated.connect(
            lambda text: self.handle_completion(
                text, self.ui.TxtSearch, self.completer, self._completing_client
            )
        )
        completer.highlighted.connect(
            lambda text: self.handle_select_client_change(text)
        )
        return completer

    def copy_text(self, text):
        self.clipboard.setText(text)
        self.statusBar().showMessage(f"Se ha copiado al portapapeles {text}", 3000)

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
        data_dir = Path(dirname)  # Asumiendo que `dirname` ya está definido correctamente
        search_data_file = data_dir / "search_data.pkl"
        sells_file = data_dir / "sells.pkl"

        print(search_data_file, search_data_file.is_file())
        print(sells_file, sells_file.is_file())

        if search_data_file.is_file() and sells_file.is_file():
            try:
                with search_data_file.open("rb") as f:
                    self.simplied_sell_notes = pickle.load(f)

                with sells_file.open("rb") as f:
                    self.sales_dict = pickle.load(f)

                self.completer_model.setStringList(self.simplied_sell_notes)

            except Exception as e:
                showFailDialog(self, f"Error al cargar los datos: {e}")
                self.simplied_sell_notes = []
                self.sales_dict = {}
        else:
            showFailDialog(self, "No se pudo cargar la información de ventas")
            self.simplied_sell_notes = []
            self.sales_dict = {}

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
        try:
            card_url = trello.add_card(
                cardName=card_name,
                desc=desc,
                labels=[info["type"]],
                members=[info["employee"]],
            )
        except:
            return "No se pudo guardar en Trello"
        return card_url

    def save_to_google(self, info):
        self.statusBar().showMessage("Guardando el Google")

        google_api = GoogleSpreadsheetApi()
        try:
            worksheet = google_api.get_worksheet()
        except Exception as e:
            worksheet = None
            showFailDialog(self,str(e))
            "☑️ Error al guardar en google"
        data = [
            [
                info["nota"],  ##Nota / factura
                info["client_name"],  ##Nombre del cliente
                info["client_phone"],  ##Telefono del cliente
                info["user_name"],  ##nombre usuario
                info["user_phone"],  ##Telefono del cliente
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
        if worksheet:
            try:
                print("escribiendo en la ultima fila")
                worksheet.write_in_last_row(data)
            except Exception as e:
                showFailDialog(self, "Ocurrió un error al guardar en Google")
                self.statusBar().showMessage("Error al guardar en Google")
                return "❌ Error al guardar en google"
        else:
            self.statusBar().showMessage("No se pudo obtener el worksheet")
            return "❌ Error al guardar en google"
        return "✅ Guardado en google"

    def save_report(self):
        result_message = []
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
        if trello_card_url != "":
            result_message.append("✅ Guardado en trello")
        else:
            result_message.append("❌ No se pudo guardar en trello")
        
        
        self.statusBar().showMessage("Guardado en trello")

        result_message.append(self.save_to_google(data))
        self.statusBar().showMessage("Guardado en google sheets")

        # Registrar Cliente en Google Contacts
        if self.ui.CheckRegisterClient.isChecked():
            try:
                self.register_contact(name=data["client_name"], phone=data["client_phone"])
                self.statusBar().showMessage(
                    f"Guardado {data["client_name"]} en Google Contacts"
                )
                result_message.append('✅ Contacto guardado en google')
            except:
                result_message.append('❌ Contacto no guardado en google')

        # Registrar Usuario en Google Contacts
        if (
            not self.ui.CheckSameUser.isChecked()
        ) and self.ui.CheckRegisterUser.isChecked():
            if self.googleContacts.verify_connection():
                try:
                    self.googleContacts.register_contact(
                        name=data["user_name"], phone=data["user_phone"]
                    )
                    self.statusBar().showMessage(
                        f"Contacto {data["user_name"]} guardado en Google Contacts"
                    )
                    result_message.append('✅ Contacto guardado en google')
                except:
                    result_message.append('❌ Contacto NO guardado en google')
            else:
                showFailDialog(self, "No se pudo conectar a Google Contacts")
                self.statusBar().showMessage("Error al conectar con Google Contacts")

        self.statusBar().showMessage("Registro guardado exitosamente", 4000)
        self.clear_inputs()
        
        
        showSuccessDialog(self, "\n ".join(str(item) for item in result_message))
        
        
        # except Exception as e:
        #     print("Error al registrar")

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