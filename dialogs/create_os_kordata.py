from os import path
from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import QDate
from ui.create_os_form_ui import Ui_create_os_form

from helpers import load_yaml_file, write_yaml
from globals import config_file, getConfig, get_current_directory
from modules.Trello.trelloConfig import trello_members
from modules.Kordata.auth import get_current_user

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog


# from gspread import *
dirname = get_current_directory()




class CreateOSKordata(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_create_os_form()
        self.ui.setupUi(self)
        self.config = getConfig()
        self.current_user = get_current_user()
        self.ui.BtnSaveDevice.clicked.connect(lambda: print('Save Device'))
        
   
        
    @staticmethod
    def launch(parent):
        dialog = CreateOSKordata(parent=parent)
        dialog.show()