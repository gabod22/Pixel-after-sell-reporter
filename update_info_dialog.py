from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QLineEdit,
    QApplication,
    QCompleter,
    QDialog
)
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt

from ui.update_data_dialog_ui import Ui_Dialog

import sys
import pandas as pd
from os import path


# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))



class UpdateInfoDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super(UpdateInfoDialog, self).__init__(*args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        

