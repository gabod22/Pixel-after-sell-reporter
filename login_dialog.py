from PySide6.QtWidgets import (
    QDialog,
)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt
from helpers import get_current_token
from ui.update_data_dialog_ui import Ui_Dialog

# from tabulate import tabulate

import sys
import pandas as pd
from os import path

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog

import requests
import time
import json
import pickle


# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable), '_internal')
elif __file__:
    dirname = path.join(path.dirname(__file__))



K_ENDPOING = "https://biz.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion-masivo"

class LoginDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dirname = path.dirname(__file__)
        self.exe_dirname = path.dirname(sys.executable)
        self.ui.BtnSubmit.clicked.connect(self.action_login)
        
    def action_login(self):
        email = self.ui.TxtEmail.text()
        password = self.ui.TxtPassword.text()
        self.login(email,password)
        
        
    def login(self,username, password):
        global currentToken
        headers = {
            "user-agent": "Pixel-kor_extraction/0.0.1",
            "Content-Type": "application/json",
        }
        payload = {
            "username": username,
            "password": password,
            "verificarEmail": True,
            "tipoDispositivo": "desktop",
        }
        response = requests.post(
            K_LOGIN_ENDPOINT,
            json=payload,
            headers=headers,
        )
        json = response.json()
        print(json)
        if json["token"]:
            currentToken = json
            # print(currentToken)
            f = open(path.join(dirname,"token_kordata.json"), "w")
            f.write(currentToken)
            print("sesion iniciada")
        else:
            
            # print(payload)
            print(
                "No se ha podido iniciar sesión, revise si no hay una sesión iniciada"
            )

            result = show_yes_no_dialog(self, "Hay sesiones abiertas", "¿Deseas cerrar todas las sesiones?")
            if result:
                self.masive_logout(json)
                print("Sesiones cerradas")
                email = self.ui.TxtEmail.text()
                password = self.ui.TxtPassword.text()
                
                self.login(email,password)
            else:
                self.close()
                print("no se han cerrado las sesiones")
                return
        self.close()
    def masive_logout(self,response):
        print('massive')
        headers = {"user-agent": "pixel/0.0.1", "Content-Type": "application/json"}
        idsBitacora = []
        usuarioId = response["idUsuario"]
        empresaId = response["bitacoraAccesoDto"]["secciones"][0]["usuario"]["empresaId"]
        for session in response["bitacoraAccesoDto"]["secciones"]:
            idsBitacora.append(session["id"])

        payload = [
            {
                "idsBitacora": idsBitacora,
                "usuarioId": usuarioId,
                "empresaId": empresaId,
            }
        ]
        
        
        response = requests.post(
            K_MASIVE_LOGOUT_ENDPOINT,
            json=payload,
            headers=headers,
        )
        print('Massive logout',payload)
        print(response.json())

    def logout(token):
        headers = {
            "user-agent": "pixel/0.0.1",
            "Content-Type": "application/json",
            "authorization": "Bearer " + token,
        }
        payload = {"token": token}
        response = requests.post(
            K_LOGOUT_ENDPOINT,
            json=payload,
            headers=headers,
        )
        print(response.json())

    
    
    
    