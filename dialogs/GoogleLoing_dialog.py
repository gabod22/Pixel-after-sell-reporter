from os import path
from PySide6.QtWidgets import (
    QDialog
)
import logging
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from ui.GoogleLinkLogin_ui import Ui_Dialog

from globals import config_file, getConfig, get_current_directory
from modules.Trello.trelloConfig import trello_members

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog


# from gspread import *
dirname = get_current_directory()




class GoogleLogin(QDialog):
    def __init__(self, parent=None, url=""):
        # Llamamos al init de QDialog pasando solo el parent de Qt
        super().__init__(parent) 
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        
        self.textUrl = url
        self.clipboard = QGuiApplication.clipboard()
        
        # Conectamos el evento del botón
        self.ui.BtnCopyURL.clicked.connect(self.copy_text)
        
    def copy_text(self):
        self.clipboard.setText(self.textUrl)
        # Opcional: imprimir en log para confirmar
        print("URL copiada al portapapeles.")
        
    @staticmethod
    def launch(parent, url):
        # Aseguramos que el parent sea un QWidget o None, no la clase de la API
        dialog = GoogleLogin(parent=parent, url=url)
        return dialog.exec() # exec() detiene la ejecución hasta cerrar el diálogo
    
    def closeEvent(self, event):
        # Aquí puedes manejar cualquier limpieza si es necesario
        event.accept()  # Acepta el evento de cierre