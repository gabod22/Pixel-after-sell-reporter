from PySide6.QtWidgets import (
    QDialog
)
from ui.create_os_form_ui import Ui_create_os_form

from globals import config_file, getConfig, get_current_directory
from modules.Kordata.auth import get_current_user

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog



from modules.Kordata.korApi import KordataApi
from modules.Kordata.kordataConfig import K_ENDPOING
from modules.Kordata.auth import get_current_user, check_valid_session

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
        self.clients = parent.clients
        self.info = info or {}
        self.set_init_state()
        self.ui.BtnCreateOs.clicked.connect(self.create_os)
        self.result_value = None
    

    def create_device(self,device: dict):

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
        print(response)
        
        return response["data"]["VehiculosGuardar"]["id"]
    
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
            "has_backup": self.ui.CbxDeviceBackup.currentText(),
            "peripherials": self.ui.TxtDevicePeripherials.text(),
            "diagnostic_days": self.ui.SpinDeviceDaigDays.value(),
            "under_warranty": self.ui.CbxDeviceWarranty.currentText(),
            "problem": self.ui.TxtDeviceProblem.toPlainText().strip(),
        }

        # Datos de orden de servicio
        os_info = {
            "ejecutive": self.ui.TxtOsEjecutive.text().strip(),
            "process_days": self.ui.SpinOsProcessDays.value(),
            "solution": self.ui.TxtOsSolution.toPlainText().strip()
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

    def create_os(self):
        self.current_user = get_current_user()
        form_data = self.getInputs()
        
        
        comentarios = (str(self.info['sell_note']) + " - " + str(self.info['type']) + " - Vendedor: " + str(self.info['seller']))


        device_info = {
            "model": form_data['device']['model'],
            "warranty": form_data['device']['under_warranty'],
            "clienteId": str(form_data['client_id']),
            "password": form_data['device']['password'],
            "serialnumber": form_data['device']["serial"],
            "peripherials": form_data['device']["peripherials"],
            "problem": str(form_data['device']['problem']).replace("\n", ""),
            "comments": comentarios,
            "backup": form_data['device']['has_backup'],
            "client_phone": str(form_data['client_phone']),
            "diagnositcs_days": form_data['device']['diagnostic_days'],
        }
        try:
            
            device_id = self.create_device(device_info)
            print(device_id)
        except Exception as e:
            print(e)
            showFailDialog(self, "No se pudo crear el dispositivo: " + str(e))
            return
        
        
        create_os_payload = {
            "variables": {},
            "query": "mutation { \n OrdenesServiciosGuardar(\n data: {"
            + "sucursalId: 1, almacenId: 1,  monedaId: 1"
            + ",clienteId: " + str(form_data['client_id'])
            + ",ordenesServiciosVehiculos: [{vehiculoId: " + str(device_id).replace("\n", "") + ", isDeleted: false}]" #Dispositivo
            + ",automotrizKms: null"
            + ',campoAdicionalTexto2: "' + str(form_data['os']['solution']) + '"' # Solucion
            + ",nombreEntrego: null"  # Orden de comrpa
            + ",ejecutivoId: " + str(self.current_user['idUsuario'])  # Ejecutivo 
            + ',comentarios: "'+ comentarios +'"'
            + ",impuestos: 0"
            + ",descuento: 0"
            + ",importeTotal: 0"
            + ",subtotal: 0"
            + ',ordenesServiciosDetalle: [{productoId: 3398, descripcion: "MANO DE OBRA GARANTÍA", precioUnitario: 0, cantidad: 1, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]'
            + "}\n  ) {\n    id\n folioPrefijo \n   }\n}",
            #Producto estructura#{productoId: 3398, descripcion: "MANO DE OBRA GARANTÍA", precioUnitario: 0, cantidad: 1, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}
        }
        print(create_os_payload)
        response = KordataApi(K_ENDPOING).post(create_os_payload)
        os_folio = response["data"]["OrdenesServiciosGuardar"]["folioPrefijo"]
        
        if os_folio:
            showSuccessDialog(self, "Se ha registrado la orden de servicio correctamente")
            self.result_value = os_folio
            self.accept()
        return response["data"]["OrdenesServiciosGuardar"]["folioPrefijo"]
        # "query": "mutation {\n  OrdenesServiciosGuardar(\n    data: {sucursalId: 1, almacenId: 1, clienteId: 5805, monedaId: 1, ordenesServiciosVehiculos: [{vehiculoId: 4403, isDeleted: false}], automotrizKms: \"Se le recomienda, no dejar el equipo apagado por mucho tiempo sin la batería\", campoAdicionalTexto2: \"Se le hizo un drenado de energia, se abrio el equipo para quitar la batería interna de reloj y la ram, se procedio a presionar el boton de encendido y se conectó el equipo, finalmente encendió, se hicieron pruebas de funcionamiento con y sin batería, el equipo funcionó bien\", nombreEntrego: \"Sin orden de compra\", ejecutivoId: 14880, comentarios: \"2\", impuestos: 0, descuento: 0, importeTotal: 0, subtotal: 0, ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 2, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]}\n  ) {\n    id\n  }\n}"

    @staticmethod
    def launch(parent, info = None):
        if check_valid_session():
            dialog = CreateOSKordata(parent=parent, info=info)
            result = dialog.exec()  # Bloquea hasta que se cierre
            if result == QDialog.Accepted:
                return dialog.result_value
        else:
            showFailDialog(parent, "No hay una sesión válida, inice sesión en kordata de nuevo")
        return None