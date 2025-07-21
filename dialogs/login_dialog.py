from PySide6.QtWidgets import QDialog
from ui.kordata_login_ui import Ui_Kordata_Login
from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
from modules.Kordata.auth import login, masive_logout
from globals import getConfig

class LoginDialog(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = Ui_Kordata_Login()
        self.ui.setupUi(self)
        self.ui.BtnSubmit.clicked.connect(self.attempt_login)
        self.config = getConfig()
        self.ui.TxtEmail.setText(self.config['KORDATA']['USERNAME'])

    def attempt_login(self):
        email = self.ui.TxtEmail.text().strip()
        password = self.ui.TxtPassword.text().strip()

        if not email or not password:
            showFailDialog(self, "Por favor, ingresa el correo y la contraseña.")
            return

        self.ui.BtnSubmit.setEnabled(False)
        session = login(email, password)

        if self.is_successful(session):
            self.handle_success(session)
        elif self.is_already_logged(session):
            self.handle_already_logged(session, email, password)
        else:
            self.handle_failure(session)

        self.ui.BtnSubmit.setEnabled(True)

    def is_successful(self, session):
        return session.get("success", False) is True

    def is_already_logged(self, session):
        return session.get("error", {}).get("type") == "already_logged"

    def handle_success(self, session):
        username = session.get("username", "usuario")
        showSuccessDialog(self, f"Sesión iniciada correctamente. Bienvenido {username}")
        self.close()

    def handle_failure(self, session):
        error = session.get("error", {})
        message = error.get("message", "Ocurrió un error desconocido al iniciar sesión.")
        showFailDialog(self, message)

    def handle_already_logged(self, session, email, password):
        if self.ui.CheckAutoClose.isChecked():
            confirm = True
        else: 
            confirm = show_yes_no_dialog(self, "Sesiones activas detectadas", "Ya hay sesiones abiertas. ¿Deseas cerrarlas?")
            
        if confirm:
            masive_logout(session["error"]["data"])
            retry_session = login(email, password)
            if self.is_successful(retry_session):
                self.handle_success(retry_session)
            else:
                self.handle_failure(retry_session)
        else:
            self.close()

    @staticmethod
    def launch(parent):
        dialog = LoginDialog(parent=parent)
        dialog.show()
