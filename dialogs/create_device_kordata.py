from os import path
from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import QDate
from ui.device_info_form_ui import Ui_create_device_form

from helpers import load_yaml_file, write_yaml
from globals import config_file, getConfig, get_current_directory
from modules.Trello.trelloConfig import trello_members

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog


# from gspread import *
dirname = get_current_directory()




class ConfigDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_create_device_form()
        self.ui.setupUi(self)
        self.config = getConfig()
        self.ui.BtnSaveDevice.clicked.connect(lambda: print('Save Device'))
        
   
        
    @staticmethod
    def launch(parent):
        dialog = ConfigDialog(parent=parent)
        dialog.show()