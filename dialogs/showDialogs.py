from .login_dialog import LoginDialog
from .config_dialog import ConfigDialog
from .getInfo_dialog import GetInfoDialog
from .addContact_dialog import AddContactDialog

def show_login_dialog(parent):
        updateDialog = LoginDialog(parent=parent)
        updateDialog.show()

def show_update_info_dialog(parent):
    updateDialog = GetInfoDialog(parent=parent)
    updateDialog.show()

def show_add_contact_dialog(parent):
    AddContact = AddContactDialog(parent=parent)
    AddContact.show()
    
def show_config_dialog(parent):
    configDialog = ConfigDialog(parent=parent)
    configDialog.show()