
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QApplication,
    QCompleter,
)
from PySide6.QtCore import QSize, Qt, QStringListModel
from PySide6.QtGui import QIcon
from PySide6.QtGui import QGuiApplication

from ui.aftersalesui_ui import Ui_MainWindow

import sys
from pathlib import Path
from datetime import datetime, timedelta
import logging

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
from helpers import  split_client_info

from globals import get_current_directory, getConfig

import pickle

from dialogs.login_dialog import LoginDialog
from dialogs.config_dialog import ConfigDialog
from dialogs.addContact_dialog import AddContactDialog
from dialogs.getInfo_dialog import GetInfoDialog
from dialogs.create_os_kordata import CreateOSKordata


from modules.Trello.trelloConfig import trello_labels, trello_members
from modules.Trello.trelloApi import TrelloApi
from modules.Trello.trello_text_templates import (
    TRELLO_DESCRIPTION_TEMPLATE,
    TRELLO_CARD_NAME_TEMPLATE,
    TRELLO_CARD_NAME_TEMPLATE_OS
)

from modules.Google.contactsApi import GoogleContactsApi
from modules.Google.sheetsApi import GoogleSpreadsheetApi

from modules.Kordata.auth import check_valid_session


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
        self.clients = {}
        self.info = {}

        self.completer = self.setup_autocomplete()
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
            (self.ui.BtnCopyNote, self.ui.TxtSellNote.text),
        ]

        for button, get_text in copy_map:
            button.clicked.connect(lambda _, g=get_text: self.copy_text(g()))

        # Conexiones del menú
        menu_actions = [
            (self.ui.actionActualizar_datos_2.triggered, lambda: GetInfoDialog.launch(self)),
            (self.ui.actionGuardar_contacto.triggered, lambda: AddContactDialog.launch(self)),
            (self.ui.actionConfiguracion.triggered, lambda: ConfigDialog.launch(self)),
            (self.ui.accionLoginKordata.triggered, lambda: LoginDialog.launch(self)),
            (self.ui.actionNueva_Orden_Servicio.triggered,lambda: CreateOSKordata.launch(self))
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

    def setup_autocomplete(self):
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

        client_name = sell_note_data["Cliente - Nombre del cliente"]
        client_phone = str(sell_note_data["phone"])
        seller = str(sell_note_data["Vendedor"])
        buy_date = date.strftime("%d/%m/%Y")

        # Set UI fields
        self.ui.TxtUserName.setText(client_name)
        self.ui.TxtUserPhone.setText(client_phone)
        self.ui.TxtClientName.setText(client_name)
        self.ui.TxtClientPhone.setText(client_phone)
        self.ui.TxtSellNote.setText(str(sell_note))
        self.ui.TxtBuyDate.setText(buy_date)
        self.ui.TxtSeller.setText(seller)
        self.ui.TxtUserName.setEnabled(False)
        self.ui.TxtUserPhone.setEnabled(False)

        # Calcular días restantes de garantía
        now = datetime.now().date()
        one_year = timedelta(days=365)
        left_days = (date + one_year - now).days

        if left_days < 0:
            self.ui.LbLeftDays.setText("Sin garantía")
        else:
            self.ui.LbLeftDays.setText(str(left_days))

        # Obtener descripciones de los items
        items = sell_note_data.get("items", [])
        items_description = [item.get("Descripcion", "") for item in items]

        if not items:
            self.ui.TxtModel.setVisible(True)
            self.ui.CbxModel.setDisabled(True)
            self.ui.TxtModel.setFocus()
        else:
            self.ui.TxtModel.setVisible(False)
            self.ui.CbxModel.setDisabled(False)

        self.ui.CbxModel.clear()
        self.ui.CbxModel.addItems(items_description)

        # Guardar datos en self.info
        self.info = {
            "sell_note": sell_note,
            "client_name": client_name,
            "client_phone": client_phone,
            "seller": seller,
            "buy_date": date,
            "warranty_days_left": left_days,
            "items": items_description
        }

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
        self.ui.TxtSellNote.setText("")
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
        clients_file = data_dir / "clients.pkl"
        
        print(search_data_file, search_data_file.is_file())
        print(sells_file, sells_file.is_file())

        if search_data_file.is_file() and sells_file.is_file():
            try:
                with search_data_file.open("rb") as f:
                    self.simplied_sell_notes = pickle.load(f)

                with sells_file.open("rb") as f:
                    self.sales_dict = pickle.load(f)
                    
                with clients_file.open("rb") as f:
                    self.clients = pickle.load(f)

                self.completer_model.setStringList(self.simplied_sell_notes)

            except Exception as e:
                showFailDialog(self, f"Error al cargar los datos: {e}")
                self.simplied_sell_notes = []
                self.sales_dict = {}
                self.clients = {}
        else:
            showFailDialog(self, "No se pudo cargar la información de ventas")
            self.simplied_sell_notes = []
            self.sales_dict = {}
            self.clients = {}

    def save_to_trello(self, info):
        trello = TrelloApi()
        self.statusBar().showMessage("Guardando en Trello")
        desc = TRELLO_DESCRIPTION_TEMPLATE.format(
            client_name=info["client_name"],
            client_phone=info["client_phone"],
            user_name=info["user_name"],
            user_phone=info["user_phone"],
            not_fac=info.get("sell_note",""),
            model=info["model"],
            issue=info["problem"],
            buy_date=info["buydate"],
            seller=info["seller"] if info["seller"] == "None" else "No especificado",
            left_days=info["left_days"],
        )
        if 'kor_os_folio' in info:
            card_name = TRELLO_CARD_NAME_TEMPLATE_OS.format(
                phone=info["user_phone"], name=info["user_name"], not_fac=info["sell_note"], service_order=info['kor_os_folio']
            )
        else:
            card_name = TRELLO_CARD_NAME_TEMPLATE.format(
                phone=info["user_phone"], name=info["user_name"], not_fac=info["sell_note"]
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
                info.get("sell_note", ""),  # Nota / factura
                info.get("kor_os_folio", ""),  # Orden de servicio
                None, # Status
                info.get("client_name", ""),  # Nombre del cliente
                info.get("client_phone", ""),  # Telefono del cliente
                info.get("user_name", ""),  # Nombre usuario
                info.get("user_phone", ""),  # Teléfono del usuario
                None, #whatsapp button
                info.get("type", ""),
                info.get("employee", ""),
                None,
                info.get("problem", ""),
                None, # Clasificacion problema
                None, # Area responsable
                info.get("solution", ""),  # Solución brindada
                None, # Cambio de equipo?
                info["seller"] if info["seller"] == "None" else "No especificado",
                info.get("model", ""),  # MODELO DEL EQUIPO
                info.get("serial_number", ""),  # NÚMERO DE SERIE
                info.get("buydate", ""),  # Fecha de compra
                None,  # Días restantes
                None,  # Inicio
                None,  # Fin
                None,  # Recursos, tiempo
                None,  # Envíos
                None,  # Costos
                None,  # Costo Total
                info.get("card_url", ""),  # URL Trello
                info.get("today", ""),  # Fecha registro
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
            "sell_note": self.ui.TxtSellNote.text(),
            "model": self.ui.CbxModel.currentText(),
            "type": self.ui.CbxType.currentText(),
            "problem": self.ui.TxtProblem.toPlainText(),
            "employee": self.ui.CbxAgent.currentText(),
            "seller": self.ui.TxtSeller.text(),
        }
        if self.config['KORDATA']['OPEN_DIALOG_CREATE_OS']:
            confirm = show_yes_no_dialog(self, "Neuva orden de servicio", "¿Deseas crear la orden de servicio?")
        else:
            confirm = False
        if confirm:
            if check_valid_session():
                
                os_folio = self.launch_save_os_dialog()
                if os_folio:
                    print('Folio: ' + os_folio)
                    data['kor_os_folio'] = os_folio
                else:
                    print("El usuario canceló o hubo un error")
                    return
            else:
                showFailDialog(self, "No tienes una sesion válda de Kordata, inicia sesión de nuevo para guardar la informaciín")
                LoginDialog.launch(self)
                return
                
        
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
                    "Guardado {} en Google Contacts".format(data["client_name"])
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
                        "Guardado {} en Google Contacts".format(data["client_name"])
                    )
                    result_message.append('✅ Contacto guardado en google')
                except:
                    result_message.append('❌ Contacto NO guardado en google')
            else:
                showFailDialog(self, "No se pudo conectar a Google Contacts")
                self.statusBar().showMessage("Error al conectar con Google Contacts")

        showSuccessDialog(self, "\n ".join(str(item) for item in result_message))
        self.statusBar().showMessage("Registro guardado exitosamente", 4000)
                
        self.clear_inputs()


    def update_config(self):
        self.config = getConfig()
        self.ui.CbxAgent.clear()
        self.ui.CbxAgent.addItems(trello_members.keys())
        self.ui.CbxAgent.setCurrentText(self.config["TRELLO_DEFAULT_AGENT"])
        self.statusBar().showMessage("Configuración actualizada", 3000)

    def launch_save_os_dialog(self):
        self.info = {
            "sell_note": self.ui.TxtSellNote.text().strip(),
            "client_name": self.ui.TxtClientName.text().strip(),
            "client_phone": self.ui.TxtClientPhone.text().strip(),
            "user_name": self.ui.TxtUserName.text().strip(),
            "user_phone": self.ui.TxtUserPhone.text().strip(),
            "seller": self.ui.TxtSeller.text().strip(),
            "buy_date": self.ui.TxtBuyDate.text().strip(),
            "model": self.ui.CbxModel.currentText().strip(),
            "warranty_days_left": self.ui.LbLeftDays.text().strip(),
            "type": self.ui.CbxType.currentText().strip(),
            "agent": self.ui.CbxAgent.currentText().strip(),
            "problem": self.ui.TxtProblem.toPlainText().strip(),
        }

        # Crear y lanzar el diálogo, pasándole la info como argumento
        return CreateOSKordata.launch(self, self.info)
if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec())