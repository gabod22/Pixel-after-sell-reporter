from os import path
from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import QDate, Qt
from ui.create_os_form_ui import Ui_create_os_form

from helpers import load_yaml_file, write_yaml
from globals import config_file, getConfig, get_current_directory
from modules.Trello.trelloConfig import trello_members
from modules.Kordata.auth import get_current_user

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog

# import requests
# import pandas as pd
# from datetime import datetime

from modules.Kordata.korApi import KordataApi
from modules.Kordata.kordataConfig import K_ENDPOING
from modules.Kordata.auth import get_current_user
# from gspread import *
dirname = get_current_directory()


class CreateOSKordata(QDialog):
    def __init__(self, parent, info, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_create_os_form()
        self.ui.setupUi(self)
        self.config = getConfig()
        self.current_user = get_current_user()
        self.ui.BtnSaveDevice.clicked.connect(lambda: print('Save Device'))
        self.clients = parent.clients
        self.info = info or {}
        self.set_init_state()
        
        

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
    
    def set_init_state(self):
        if self.info:
            
            self.ui.TxtOsEjecutive.setText(self.current_user['nombre'])
            self.ui.TxtClientName.setText(self.info['user_name'])
            self.ui.TxtClientPhone.setText(self.info['user_phone'])
            self.ui.TxtDeviceModel.setText(self.info['model'])
            
            if self.info['type'] == "Garantía":
                self.ui.CbxDeviceWarranty.setCurrentText('SI')
            self.ui.TxtDeviceProblem.setPlainText(self.info['problem'])

    def getInputs(self) -> dict:
        # Obtener datos del cliente
        client_name = self.ui.TxtClientName.text().strip()
        client_phone = self.ui.TxtClientPhone.text().strip()

        try:
            client_id = self.clients[client_name]["id"]
        except KeyError:
            raise Exception(f"Cliente '{client_name}' no encontrado")

        # Datos del dispositivo
        device_info = {
            "model": self.ui.TxtDeviceModel.text().strip(),
            "serial": self.ui.TxtDeviceSerial.text().strip(),
            "password": self.ui.TxtDevicePass.text().strip(),
            "has_backup": self.ui.CbxDeviceBackup.isChecked(),
            "diagnostic_days": self.ui.SpinDeviceDaigDays.value(),
            "under_warranty": self.ui.CbxDeviceWarranty.isChecked(),
            "problem": self.ui.TxtDeviceProblem.text().strip(),
            "comment": self.ui.TxtDeviceComment.text().strip(),
        }

        # Datos de orden de servicio
        os_info = {
            "ejecutive": self.ui.TxtOsEjecutive.text().strip(),
            "process_days": self.ui.SpinOsProcessDays.value(),
            "solution": self.ui.TxtOsSolution.text().strip()
        }

        # Combinar todo en un dict final
        form_data = {
            "client_id": client_id,
            "client_name": client_name,
            "client_phone": client_phone,
            "device": device_info,
            "os": os_info
        }

        return form_data

    # def create_os():
        
        
        
    #     comentarios = (str(os["NOTA / FACTURA"]) + " - " + str(os["Soporte O GARANTÍA"]) + " - Vendedor: " + str(os["VENDEDOR"]))


    #     device_info = {
    #         "model": os["MODELO DE EQUIPO"],
    #         "warranty": device["WARRANTY"],
    #         "clienteId": str(client_id),
    #         "password": device["PASSWORD"],
    #         "serialnumber": device["SERIALNUMBER"],
    #         "devices": device["PERIPHERALS"],
    #         "problem": str(os["PROBLEM"]).replace("\n", ""),
    #         "comments": comentarios,
    #         "backup": "NO",
    #         "client_phone": str(os["CONTACTO"]),
    #         "diagnositcs_days": "null",
    #     }

    #     device_id = create_device(device_info)
        
        
    #     print(device_id)
        
    #     create_os_payload = {
    #         "variables": {},
    #         "query": "mutation { \n OrdenesServiciosGuardar(\n data: {"
    #         + "sucursalId: 1, almacenId: 1,  monedaId: 1"
    #         + ",clienteId: " + str(client_id)
    #         + ",ordenesServiciosVehiculos: [{vehiculoId: " + str(device_id).replace("\n", "") + ", isDeleted: false}]" #Dispositivo
    #         + ",automotrizKms: null"
    #         + ',campoAdicionalTexto2: "' + str(os["SOLUCIÓN BRINDADA"]).replace("\n", "") + '"'  # Solucion
    #         + ",nombreEntrego: null"  # Orden de comrpa
    #         + ",ejecutivoId: " + str(curent_user_id)  # Ejecutivo 
    #         + ',comentarios: "2"'
    #         + ",impuestos: 0"
    #         + ",descuento: 0"
    #         + ",importeTotal: 0"
    #         + ",subtotal: 0"
    #         + ',ordenesServiciosDetalle: []'
    #         + "}\n  ) {\n    id\n folioPrefijo \n   }\n}",
    #         #Producto estructura#{productoId: 3398, descripcion: "MANO DE OBRA GARANTÍA", precioUnitario: 0, cantidad: 1, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}
    #     }
    #     response = KordataApi(K_ENDPOING).post(create_os_payload)
    #     print(response.json()["data"]["OrdenesServiciosGuardar"]["folioPrefijo"])
    #     return response.json()["data"]["OrdenesServiciosGuardar"]["folioPrefijo"]
    #     # "query": "mutation {\n  OrdenesServiciosGuardar(\n    data: {sucursalId: 1, almacenId: 1, clienteId: 5805, monedaId: 1, ordenesServiciosVehiculos: [{vehiculoId: 4403, isDeleted: false}], automotrizKms: \"Se le recomienda, no dejar el equipo apagado por mucho tiempo sin la batería\", campoAdicionalTexto2: \"Se le hizo un drenado de energia, se abrio el equipo para quitar la batería interna de reloj y la ram, se procedio a presionar el boton de encendido y se conectó el equipo, finalmente encendió, se hicieron pruebas de funcionamiento con y sin batería, el equipo funcionó bien\", nombreEntrego: \"Sin orden de compra\", ejecutivoId: 14880, comentarios: \"2\", impuestos: 0, descuento: 0, importeTotal: 0, subtotal: 0, ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 2, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]}\n  ) {\n    id\n  }\n}"

    @staticmethod
    def launch(parent, info = None):
        dialog = CreateOSKordata(parent=parent, info=info)
        dialog.show()