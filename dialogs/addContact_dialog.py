from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

from pathlib import Path
from ui.add_contact_dialog_ui import Ui_Dialog
from googleapiclient.errors import HttpError
from dialogs import showSuccessDialog, showFailDialog
from globals import config_file, getConfig, get_current_directory
from modules.Google.contactsApi import GoogleContactsApi
import logging

dirname = get_current_directory()
class AddContactDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.BtnSaveContact.clicked.connect(self.save_contact)
        self.ui.BtnCancel.clicked.connect(self.close)
        self.setFixedHeight(74)
        try:
            credentials_path = Path(dirname) / "credentials.json"
            token_path =Path(dirname) / "token.json"
            self.googleContacts = GoogleContactsApi(self,str(token_path), str(credentials_path))
        except Exception as e:
            logging.error(f"Error cargando sesión de google contacts en AddContact: {e}")
            showFailDialog(
                self, "No se pudo obtener la información de inicio de sesión"
            )

    def save_contact(self):
        name = self.ui.TxtContactName.text().strip()
        phone = self.ui.TxtContactPhone.text().strip()
        if (self.ui.TxtContactName.text() != "" or self.ui.TxtContactName.text() != ""):

            try:
                if self.googleContacts.verify_connection():
                    self.googleContacts.register_contact(name=name, phone=phone)
                    showSuccessDialog(self, "Contacto registrado correctamente")
                    self.close()
                else:
                    showFailDialog(self, "No se pudo conectar a Google Contacts")
                    self.parent.statusBar().showMessage("Error al conectar con Google Contacts")
            except HttpError as err:
                logging.error(f"Error HTTP al guardar contacto: {err}")
                showFailDialog(self, "No se pudo registrar el contacto")
            except Exception as e:
                logging.error(f"Error inesperado al guardar contacto: {e}")
                showFailDialog(self, "Ocurrió un error inesperado al registrar el contacto")
        else:
            showFailDialog(self, "Por favor, complete todos los campos")
    
    @staticmethod
    def launch(parent):
        dialog = AddContactDialog(parent=parent)
        dialog.show()
