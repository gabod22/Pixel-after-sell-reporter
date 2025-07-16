from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

from ui.add_contact_dialog_ui import Ui_Dialog
from googleapiclient.errors import HttpError
from dialogs import showSuccessDialog, showFailDialog


class AddContactDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.googleContacts = self.parent.googleContacts
        self.ui.BtnSaveContact.clicked.connect(self.save_contact)
        self.ui.BtnCancel.clicked.connect(self.close)
        self.setFixedHeight(74)
        

        

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
                    self.statusBar().showMessage("Error al conectar con Google Contacts")
            except HttpError as err:
                print(err)
                showFailDialog(self, "No se pudo registrar el contacto")
        else:
            showFailDialog(self, "Por favor, complete todos los campos")
    
    @staticmethod
    def launch(parent):
        dialog = AddContactDialog(parent=parent)
        dialog.show()
