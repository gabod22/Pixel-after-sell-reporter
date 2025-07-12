import requests
from os import path
from globals import get_current_directory
from dialogs import show_yes_no_dialog
import json

from .kordataConfig import (
    K_LOGIN_ENDPOINT,
    K_LOGOUT_ENDPOINT,
    K_MASIVE_LOGOUT_ENDPOINT,
)
dirname = get_current_directory()

headers = {"user-agent": "pixel-reporter/0.0.1", "Content-Type": "application/json"}

def login(username, password):

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
    data_response = response.json()
    if data_response["token"]:        
        with open(path.join(dirname,"token_kordata.json"), 'w', encoding='utf-8') as f:
            json.dump(data_response, f, ensure_ascii=False, indent=4)
        print("sesion iniciada")
        return True, data_response
    else:
        
        # print(payload)
        print(
            "No se ha podido iniciar sesión, revise si no hay una sesión iniciada"
        )

        return False, data_response
    
def masive_logout(response):
    print('Cerrando sesiones masivamente')
    print(response)
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
    
    headers.update({"Authorization": f"Bearer {token}"})
    
    payload = {"token": token}
    response = requests.post(
        K_LOGOUT_ENDPOINT,
        json=payload,
        headers=headers,
    )
    print(response.json())
    
def get_current_token():
    try:
        f = open(path.join(dirname,"token_kordata.json"), "r")
        kordata_session = json.loads(f.read())
        # print(kordata_session)
        return kordata_session["token"]
    except:
        print('No pude obtener el token')