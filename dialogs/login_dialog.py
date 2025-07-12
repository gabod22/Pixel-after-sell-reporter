from PySide6.QtWidgets import (
    QDialog,
)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt

from ui.update_data_dialog_ui import Ui_Dialog

# from tabulate import tabulate

import sys
import pandas as pd
from os import path

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
from globals import get_current_directory
# from gspread import *
dirname = get_current_directory()

from modules.Kordata.auth import login, masive_logout




class LoginDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.BtnSubmit.clicked.connect(self.action_login)
        
    def action_login(self):
        email = self.ui.TxtEmail.text()
        password = self.ui.TxtPassword.text()
        logged, session = login(email,password)
        
        if logged:
            showSuccessDialog(self, "Sesión iniciada correctamente")
            self.close()
            self.parent.update_data()
        else:
            logoff = show_yes_no_dialog(self, "Hay sesiones abiertas", "¿Deseas cerrar todas las sesiones?")
            if logoff:
                masive_logout(session)
                print("Sesiones cerradas")
                login(email,password)
            else:
                self.close()
                print("no se han cerrado las sesiones")
                return
        self.close()
        
        
    

    
    
    
    