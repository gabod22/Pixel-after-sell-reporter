from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QLineEdit,
    QApplication,
    QCompleter,
    QDialog,
)
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt

from ui.add_contact_dialog_ui import Ui_Dialog
# from tabulate import tabulate

import sys
import pandas as pd
from os import path

from google_contacts import get_credentials_people_api
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dialogs import showSuccessDialog, showFailDialog

import pickle

# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))


class AddContactDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dirname = path.dirname(__file__)
        self.exe_dirname = path.dirname(sys.executable)
        self.accepted.connect(self.save_contact)
        
        self.creds_people = self.parent.creds_people

        

    def save_contact(self):
        try:
            if (self.ui.TxtContactName.text() == "" or self.ui.TxtContactName.text() == ""):
                return
            
            service = build("people", "v1", credentials=self.creds_people)
            service.people().createContact( body={
            "names": [
                {
                    "givenName": self.ui.TxtContactName.text()
                }
            ],
            "phoneNumbers": [
                {
                    'value': self.ui.TxtContactPhone.text()
                }
            ],}).execute()
        except HttpError as err:
            print(err)
            showFailDialog(self.parent, "No se pudo registrar el contacto")
            
    
    