import requests
from os import path
from globals import get_current_directory
from dialogs import show_yes_no_dialog
import json
from .kordataConfig import (
    K_ENDPOING,
    K_LOGIN_ENDPOINT,
    K_LOGOUT_ENDPOINT,
    K_MASIVE_LOGOUT_ENDPOINT,
)
dirname = get_current_directory()

headers = {"user-agent": "pixel-reporter/0.0.1", "Content-Type": "application/json"}

error_messages = {
    "pass_email_wrong": "Correo electrónico y/o la contraseña son incorrectos.",
    "invalid_format": "El correo no es valido. Por favor intente de nuevo. Ejemplo: Abc123@dominio.com.mx",
    "already_logged": "Ya hay sesiones iniciadas, por favor cierre las sesiones activas",
    "void_input": "El parámetro username no debe ser vacío"
}

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
    print(data_response)
    if "token" in data_response and data_response["token"] != None:        
        with open(path.join(dirname,"token_kordata.json"), 'w', encoding='utf-8') as f:
            json.dump(data_response, f, ensure_ascii=False, indent=4)
        return {"success": True, "username": data_response["nombre"]}
    else:
        if "idUsuario" in data_response:
        # Verifica si ya hay sesiones iniciadas
            if len(data_response["bitacoraAccesoDto"]["secciones"]) > 0:
                return {"error": {"type": "already_logged", "message":error_messages["already_logged"], "data": data_response}}
        
        elif "errorMessage" in data_response["errorMessage"]:
            return {"error": {"type": "pass_email_wrong", "message":data_response["errorMessage"]}}
        else:
            return {"error": {"type": "unknown", "message": data_response["errorMessage"]}}
        
        
    
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

def check_valid_session():
    query = {"variables":{},"query":"{\n  BasesReportesGenerarConTerminosBusqueda(\n    reporteId: 894\n    terminosBusqueda: [{baseReporteColumnaId: 8564, terminoBusqueda: null, operador: null, ordenamiento: \"DESC\"}]\n    paginadoInformacion: {numeroPagina: 1, registrosPorPagina: 1}\n  ) {\n    datosListasSeleccion\n    paginadoCount\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      basesReportesColumnas {\n        id\n        seLect\n        tablaRelacionId\n        basesCampos {\n          nombreColumnaCamelcase\n        }\n      }\n    }\n  }\n}"}

    if get_current_token():
        
        headers = {"user-agent": "pixel-reporter/0.0.1", "Content-Type": "application/json", "authorization": "Bearer " + get_current_token(),}
    else:
        return False
    r = requests.post(
        K_ENDPOING,
        json=query,
        headers=headers,
    )
    r= r.json()
    print(r)
    if "data" in r:
        return True
    return False
    

def get_current_token():
    try:
        f = open(path.join(dirname,"token_kordata.json"), "r")
        kordata_session = json.loads(f.read())
        # print(kordata_session)
        return kordata_session["token"]
    except:
        print('No pude obtener el token')
        return None
        
def get_current_user():
    try:
        f = open(path.join(dirname,"token_kordata.json"), "r")
        kordata_session = json.loads(f.read())
        return kordata_session
    except:
        print('No pude obtener el usuario actual')
        return None