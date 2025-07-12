from helpers import get_current_token
import requests
import pandas as pd
from datetime import datetime


USERNAME = "consultoria@pixel-lap.com"
PASS = "Pixel12345"

START_DATE = "2022-01-01"

K_ENDPOING = "https://biz.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion-masivo"
ejecutives  = [{"id":8058,"name":"ALAN  PONGA","Estatus":"B"},{"id":8068,"name":"ALAN PONGA","Estatus":"A"},{"id":3830,"name":"Alexis Leonel Negrete","Estatus":"B"},{"id":8717,"name":"ANA PAULA  MIRANDA","Estatus":"B"},{"id":8859,"name":"ANA PAULA MIRANDA","Estatus":"B"},{"id":10842,"name":"BRIAN DIAZ","Estatus":"B"},{"id":8074,"name":"CARMEN OLVERA","Estatus":"A"},{"id":14418,"name":"CORAL VAZQUEZ","Estatus":"A"},{"id":20817,"name":"Damaris Vera","Estatus":"A"},{"id":8073,"name":"DANIEL RIOS","Estatus":"B"},{"id":8059,"name":"DANIEL RIOS","Estatus":"B"},{"id":20003,"name":"Derek Gonzalez","Estatus":"B"},{"id":20005,"name":"Derek Gonzalez","Estatus":"A"},{"id":17935,"name":"Derek Gonzalez","Estatus":"B"},{"id":11540,"name":"Edwin Martínez","Estatus":"A"},{"id":4642,"name":"er CESAR","Estatus":"B"},{"id":22637,"name":"Esteff Huerta","Estatus":"A"},{"id":14257,"name":"Fatima Olalde","Estatus":"A"},{"id":23990,"name":"Fernando López","Estatus":"A"},{"id":12866,"name":"Frida Ruiz","Estatus":"B"},{"id":12865,"name":"FRIDA RUIZ","Estatus":"B"},{"id":14880,"name":"GABRIEL DIAZ","Estatus":"A"},{"id":3815,"name":"IMOBILE ","Estatus":"B"},{"id":13464,"name":"KARLA PALACIOS","Estatus":"B"},{"id":14985,"name":"Miguel Padilla","Estatus":"A"},{"id":11342,"name":"OSWALDO DE SANTIAGO","Estatus":"A"},{"id":14878,"name":"PEDRO COPADO","Estatus":"A"},{"id":8077,"name":"SERGIO  CAMACHO","Estatus":"A"},{"id":8036,"name":"SERGIO CAMACHO ANGULO ","Estatus":"B"},{"id":8131,"name":"SERVICIO TECNICO","Estatus":"B"},{"id":10772,"name":"SUJETO ACUÑA","Estatus":"B"},{"id":3829,"name":"Vantas02 Mostrador","Estatus":"B"},{"id":3817,"name":"Ventas 01","Estatus":"B"},{"id":23253,"name":"Vicente Puga","Estatus":"B"}]

def get_clients():
        try:
            currentToken = get_current_token()

            headers = {
                "user-agent": "pixel/0.0.1",
                "Content-Type": "application/json",
                "authorization": "Bearer " + currentToken,
            }
            query_report_list_sales_notes = {
                "variables": {},
                "query": '{\n  BasesReportesGenerarConTerminosBusqueda(\n    reporteId: 894\n    terminosBusqueda: [{baseReporteColumnaId: 8564, terminoBusqueda: null, operador: null, ordenamiento: "DESC"}]\n    paginadoInformacion: {numeroPagina: 1, registrosPorPagina: 100000}\n  ) {\n    datosListasSeleccion\n    paginadoCount\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      basesReportesColumnas {\n        id\n        seLect\n      }\n    }\n  }\n}',
            }
            response = requests.post(
                K_ENDPOING,
                json=query_report_list_sales_notes,
                headers=headers,
            )

            clients = response.json()["data"]["BasesReportesGenerarConTerminosBusqueda"][
                "resultadoReporteHashmap"
            ]
            clients.pop(0)
            mapped_clients = {}
            for client in clients:
                mapped_clients[client['Nombre del cliente']] = client
            # print(mapped_clients)
            return mapped_clients
        except:
            pass


def getOs():
    try:
        orders = pd.read_excel('postventas.xlsx')
        orders_arr = orders.to_dict('records')
        print(orders)
    except Exception as e:
        raise "No se pudo abrir el documento:" + e
    
    # print(orders_arr)
    return orders_arr

def save_device_to_kordata(device:dict):
    currentToken = get_current_token()

    headers = {
        "user-agent": "pixel/0.0.1",
        "Content-Type": "application/json",
        "authorization": "Bearer " + currentToken,
    }
    payload = {
        "variables": {},
        "query": 'mutation {\n VehiculosGuardar( data: { ' +
        'modelo: "' + device['model'] + '"' + #Modelo
        ', color: "Si"' +  #Garantia
        ', clienteId: ' + str(device['clienteId']) + #Cliente
        ', placas: "' + str(device['password']) + '"' + #Contraseña
        ', marca: "' + str(device['serialnumber']) +'"' + #Numero de serie
        ', motor: "' + device['devices'] +'"' + # Perifericos
        ', ano: "' + device['problem'] +'"' + # Problema
        ', serie: "' + device['comments'] +'"' + # Observaciones
        ', nombreAseguradora: "' + device['backup'] + '"' + # Respaldo
        ', numeroEconomico: "' + str(device['client_phone']) + '"' + # Telefono
        ', numeroPolizaSeguro: "' + str(device['diagnositcs_days']) +'"' + #
        '}\n  ) {\nid\n}\n}' 
    }   
    print(payload["query"])
    response = requests.post(
        K_ENDPOING,
        json=payload,
        headers=headers,
    )
    print(response.json())
    # print(payload)
    return response.json()

clients = get_clients()


def save_os_to_kordata(os: dict):
    currentToken = get_current_token()
    
    

    headers = {
        "user-agent": "pixel/0.0.1",
        "Content-Type": "application/json",
        "authorization": "Bearer " + currentToken,
    }
    try:
        client_id = clients[os['CLIENTE']]['id']
    except:
        raise Exception(os['CLIENTE'] +" Cliente no encontrado")
    comentarios = str(os['NOTA / FACTURA']) + " - " + str(os['Soporte O GARANTÍA']) + " - Vendedor: " + str(os['VENDEDOR'])
    print(client_id)
    device_payload = {
        'model': os['MODELO DE EQUIPO'],
        'warranty': "SI",
        'clienteId': str(client_id),
        'password': "NA",
        'serialnumber': "NA",
        'devices': "NA",
        'problem': str(os['DESCRIPCIÓN DEL PROBLEMA']).replace('\n',""),
        'comments': comentarios,
        'backup': "NO",
        'client_phone': str(os['CONTACTO']),
        'diagnositcs_days': 'null'
        
    }
    
    
    device = save_device_to_kordata(device_payload)
    deviceId = device['data']['VehiculosGuardar']['id']
    print(deviceId)
    payload = {
        "variables": {},
        "query": 'mutation { \n OrdenesServiciosGuardar(\n data: {' +
            'sucursalId: 1, almacenId: 1,  monedaId: 1'+ 
            ',clienteId: ' + str(client_id) + 
            ',ordenesServiciosVehiculos: [{vehiculoId: '+ str(deviceId).replace('\n',"") + ', isDeleted: false}]' +
            ',automotrizKms: null' +
            ',campoAdicionalTexto2: "'+ str(os['SOLUCIÓN BRINDADA']).replace('\n',"") + '"' + #Solucion
            ',nombreEntrego: null' + #Orden de comrpa
            ',ejecutivoId: 14880'+ #Ejecutivo gabriel diaz - 14880
            ',comentarios: "2"' +
            ',impuestos: 0' +
            ',descuento: 0' +
            ',importeTotal: 0' +
            ',subtotal: 0' +
            ',ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 1, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]' +
            '}\n  ) {\n    id\n folioPrefijo \n   }\n}',
    }
    print(payload)
    response = requests.post(
        K_ENDPOING,
        json=payload,
        headers=headers,
    )
    print (response.json()['data']['OrdenesServiciosGuardar']['folioPrefijo'])
    return response.json()['data']['OrdenesServiciosGuardar']['folioPrefijo']
    # "query": "mutation {\n  OrdenesServiciosGuardar(\n    data: {sucursalId: 1, almacenId: 1, clienteId: 5805, monedaId: 1, ordenesServiciosVehiculos: [{vehiculoId: 4403, isDeleted: false}], automotrizKms: \"Se le recomienda, no dejar el equipo apagado por mucho tiempo sin la batería\", campoAdicionalTexto2: \"Se le hizo un drenado de energia, se abrio el equipo para quitar la batería interna de reloj y la ram, se procedio a presionar el boton de encendido y se conectó el equipo, finalmente encendió, se hicieron pruebas de funcionamiento con y sin batería, el equipo funcionó bien\", nombreEntrego: \"Sin orden de compra\", ejecutivoId: 14880, comentarios: \"2\", impuestos: 0, descuento: 0, importeTotal: 0, subtotal: 0, ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 2, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]}\n  ) {\n    id\n  }\n}"

# first_order = getOs()[2]

# save_os_to_kordata(first_order)
# print(get_clients())
for os in getOs():
    print(os)
    try:
        folio = save_os_to_kordata(os)
        # print("Orden guardada")
        # print("-------------------------------------------------")
        print(os['NOTA / FACTURA'],",", folio)
        
    except Exception as e:
        print(e)
        continue