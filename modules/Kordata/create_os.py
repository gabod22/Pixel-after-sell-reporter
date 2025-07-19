from helpers import get_current_token
import requests
import pandas as pd
from datetime import datetime

from .korApi import KordataApi
from .kordataConfig import K_ENDPOING

from .auth import get_current_user

ejecutives = [
    {"id": 8058, "name": "ALAN  PONGA", "Estatus": "B"},
    {"id": 8068, "name": "ALAN PONGA", "Estatus": "A"},
    {"id": 3830, "name": "Alexis Leonel Negrete", "Estatus": "B"},
    {"id": 8717, "name": "ANA PAULA  MIRANDA", "Estatus": "B"},
    {"id": 8859, "name": "ANA PAULA MIRANDA", "Estatus": "B"},
    {"id": 10842, "name": "BRIAN DIAZ", "Estatus": "B"},
    {"id": 8074, "name": "CARMEN OLVERA", "Estatus": "A"},
    {"id": 14418, "name": "CORAL VAZQUEZ", "Estatus": "A"},
    {"id": 20817, "name": "Damaris Vera", "Estatus": "A"},
    {"id": 8073, "name": "DANIEL RIOS", "Estatus": "B"},
    {"id": 8059, "name": "DANIEL RIOS", "Estatus": "B"},
    {"id": 20003, "name": "Derek Gonzalez", "Estatus": "B"},
    {"id": 20005, "name": "Derek Gonzalez", "Estatus": "A"},
    {"id": 17935, "name": "Derek Gonzalez", "Estatus": "B"},
    {"id": 11540, "name": "Edwin Martínez", "Estatus": "A"},
    {"id": 4642, "name": "er CESAR", "Estatus": "B"},
    {"id": 22637, "name": "Esteff Huerta", "Estatus": "A"},
    {"id": 14257, "name": "Fatima Olalde", "Estatus": "A"},
    {"id": 23990, "name": "Fernando López", "Estatus": "A"},
    {"id": 12866, "name": "Frida Ruiz", "Estatus": "B"},
    {"id": 12865, "name": "FRIDA RUIZ", "Estatus": "B"},
    {"id": 14880, "name": "GABRIEL DIAZ", "Estatus": "A"},
    {"id": 3815, "name": "IMOBILE ", "Estatus": "B"},
    {"id": 13464, "name": "KARLA PALACIOS", "Estatus": "B"},
    {"id": 14985, "name": "Miguel Padilla", "Estatus": "A"},
    {"id": 11342, "name": "OSWALDO DE SANTIAGO", "Estatus": "A"},
    {"id": 14878, "name": "PEDRO COPADO", "Estatus": "A"},
    {"id": 8077, "name": "SERGIO  CAMACHO", "Estatus": "A"},
    {"id": 8036, "name": "SERGIO CAMACHO ANGULO ", "Estatus": "B"},
    {"id": 8131, "name": "SERVICIO TECNICO", "Estatus": "B"},
    {"id": 10772, "name": "SUJETO ACUÑA", "Estatus": "B"},
    {"id": 3829, "name": "Vantas02 Mostrador", "Estatus": "B"},
    {"id": 3817, "name": "Ventas 01", "Estatus": "B"},
    {"id": 23253, "name": "Vicente Puga", "Estatus": "B"},
]





def create_device(device: dict):

    post_save_device = {
        "variables": {},
        "query": "mutation {\n VehiculosGuardar( data: { "
        + 'modelo: "' + str(device["model"]) + '"'  # Modelo
        + ', color: "' + str(device["warranty"]) + '"'  # Garantia
        + ', clienteId: ' + str(device["clienteId"])  # Cliente
        + ', placas: "' + str(device["password"]) + '"'  # Contraseña
        + ', marca: "' + str(device["serialnumber"]) + '"'  # Numero de serie
        + ', motor: "' + str(device["peripherials"]) + '"'  # Perifericos
        + ', ano: "' + str(device["problem"]) + '"'  # Problema
        + ', serie: "' + str(device["comments"]) + '"'  # Observaciones
        + ', nombreAseguradora: "' + str(device["backup"]) + '"'  # Respaldo
        + ', numeroEconomico: "' + str(device["client_phone"]) + '"'  # Telefono
        + ', numeroPolizaSeguro: "' + str(device["diagnositcs_days"]) + '"'  #Dias de diagnostico
        + "}\n  ) {\nid\n}\n}",
    }
    response = response = KordataApi(K_ENDPOING).post(post_save_device)
    
    return response.json()["data"]["VehiculosGuardar"]["id"]



def create_os(os: dict):
    curent_user_id = get_current_user()['idUsuario']
    try:
        
        client_id = clients[os["CLIENTE"]]["id"]
    except:
        raise Exception(os["CLIENTE"] + " Cliente no encontrado")
    
    comentarios = (str(os["NOTA / FACTURA"]) + " - " + str(os["Soporte O GARANTÍA"]) + " - Vendedor: " + str(os["VENDEDOR"]))


    device_info = {
        "model": os["MODELO DE EQUIPO"],
        "warranty": device["WARRANTY"],
        "clienteId": str(client_id),
        "password": device["PASSWORD"],
        "serialnumber": device["SERIALNUMBER"],
        "devices": device["PERIPHERALS"],
        "problem": str(os["PROBLEM"]).replace("\n", ""),
        "comments": comentarios,
        "backup": "NO",
        "client_phone": str(os["CONTACTO"]),
        "diagnositcs_days": "null",
    }

    device_id = create_device(device_info)
    
    
    print(device_id)
    
    create_os_payload = {
        "variables": {},
        "query": "mutation { \n OrdenesServiciosGuardar(\n data: {"
        + "sucursalId: 1, almacenId: 1,  monedaId: 1"
        + ",clienteId: " + str(client_id)
        + ",ordenesServiciosVehiculos: [{vehiculoId: " + str(device_id).replace("\n", "") + ", isDeleted: false}]" #Dispositivo
        + ",automotrizKms: null"
        + ',campoAdicionalTexto2: "' + str(os["SOLUCIÓN BRINDADA"]).replace("\n", "") + '"'  # Solucion
        + ",nombreEntrego: null"  # Orden de comrpa
        + ",ejecutivoId: " + str(curent_user_id)  # Ejecutivo 
        + ',comentarios: "2"'
        + ",impuestos: 0"
        + ",descuento: 0"
        + ",importeTotal: 0"
        + ",subtotal: 0"
        + ',ordenesServiciosDetalle: [{productoId: 3398, descripcion: "MANO DE OBRA GARANTÍA", precioUnitario: 0, cantidad: 1, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]'
        + "}\n  ) {\n    id\n folioPrefijo \n   }\n}",
    }
    response = KordataApi(K_ENDPOING).post(create_os_payload)
    print(response.json()["data"]["OrdenesServiciosGuardar"]["folioPrefijo"])
    return response.json()["data"]["OrdenesServiciosGuardar"]["folioPrefijo"]
    # "query": "mutation {\n  OrdenesServiciosGuardar(\n    data: {sucursalId: 1, almacenId: 1, clienteId: 5805, monedaId: 1, ordenesServiciosVehiculos: [{vehiculoId: 4403, isDeleted: false}], automotrizKms: \"Se le recomienda, no dejar el equipo apagado por mucho tiempo sin la batería\", campoAdicionalTexto2: \"Se le hizo un drenado de energia, se abrio el equipo para quitar la batería interna de reloj y la ram, se procedio a presionar el boton de encendido y se conectó el equipo, finalmente encendió, se hicieron pruebas de funcionamiento con y sin batería, el equipo funcionó bien\", nombreEntrego: \"Sin orden de compra\", ejecutivoId: 14880, comentarios: \"2\", impuestos: 0, descuento: 0, importeTotal: 0, subtotal: 0, ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 2, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]}\n  ) {\n    id\n  }\n}"
