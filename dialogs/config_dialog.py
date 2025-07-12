from PySide6.QtWidgets import (
    QDialog,
)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt
from ui.configDialog_ui import Ui_ConfigDialog

# from tabulate import tabulate

import sys
import pandas as pd
from os import path

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog


from globals import get_current_directory

# from gspread import *
dirname = get_current_directory()




class ConfigDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_ConfigDialog()
        self.ui.setupUi(self)
        self.ui.BtnSubmit.clicked.connect(self.action_login)
        
    