from os import path
from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import QDate
from ui.configDialog_ui import Ui_ConfigDialog

from helpers import load_yaml_file, write_yaml
from globals import config_file, getConfig, get_current_directory
from modules.Trello.trelloConfig import trello_members

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
import logging


# from gspread import *
dirname = get_current_directory()




class ConfigDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_ConfigDialog()
        self.ui.setupUi(self)
        self.config = getConfig()
        self.ui.BtnSaveConfig.clicked.connect(self.save_config)
        self.ui.CbxAgents.addItems(trello_members.keys())
        self.set_config()
        
    def save_config(self):

        self.config['KORDATA']['USERNAME'] = self.ui.TxtKordataUser.text()
        self.config['KORDATA']['START_DATE'] = self.ui.dateKordataStartDate.text()
        self.config['TRELLO_DEFAULT_AGENT'] = self.ui.CbxAgents.currentText()
        self.config['KORDATA']['AUTOLOGIN'] = self.ui.ChkAutoLogin.isChecked()
        self.config['KORDATA']['OPEN_DIALOG_CREATE_OS'] = self.ui.ChkDialogCreateOS.isChecked()

        

        try:
            write_yaml(config_file, self.config)
            # self.parent.update_config()
            showSuccessDialog(self,'Se cambio la configuracion correctamente')
            self.parent.update_config()
        except Exception as e:
            logging.error(f"Error al guardar configuración: {e}", exc_info=True)
            showFailDialog(self,
                'No se guardo la configuracion, pruebe manualmente')
            
            
    def set_config(self):
        self.ui.TxtKordataUser.setText(self.config['KORDATA']['USERNAME'])
        date = QDate.fromString(self.config['KORDATA']['START_DATE'], "dd/MM/yyyy")
        self.ui.dateKordataStartDate.setDate(date)
        self.ui.CbxAgents.setCurrentText(self.config['TRELLO_DEFAULT_AGENT'])
        self.ui.ChkAutoLogin.setChecked(self.config['KORDATA']['AUTOLOGIN'])
        self.ui.ChkDialogCreateOS.setChecked(self.config['KORDATA'].get('OPEN_DIALOG_CREATE_OS', True))
        
    @staticmethod
    def launch(parent):
        dialog = ConfigDialog(parent=parent)
        dialog.show()