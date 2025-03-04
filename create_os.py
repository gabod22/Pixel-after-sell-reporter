from helpers import get_current_token
import requests

USERNAME = "consultoria@pixel-lap.com"
PASS = "Pixel12345"

START_DATE = "2022-01-01"

K_ENDPOING = "https://biz.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion-masivo"

dvice_data = {
    "modelo": "DELL RUGGED", # Modelo
    "color": "NO", # Garantía
    "clienteId": 5805, # Cliente
    "placas": "NA", # Contraseña
    "marca": "DESCONOCIDO", 
    "motor": "SI, CARGADOR", #Perifericos
    "ano": "SE LE CAMBIO LA BATERÍA PORQUE YA NO TENIA ENERGIA, PERO YA NO ENCENDIÓ", # Problema
    "serie": "VINO POR PAQUETERÍA", # Observaciones
    "nombreAseguradora": "NO", 
    "numeroEconomico": "56 1915 9383", #Telefono
    "numeroPolizaSeguro": "4", 
    
}

def save_device_to_kordata():
    currentToken = get_current_token()

    headers = {
        "user-agent": "pixel/0.0.1",
        "Content-Type": "application/json",
        "authorization": "Bearer " + currentToken,
    }
    payload = {
        "variables": {},
        "query": "mutation {\n  VehiculosGuardar(\n    data: {modelo: \"DELL RUGGED\", color: \"NO\", clienteId: 5805, placas: \"NA\", marca: \"DESCONOCIDO\", motor: \"SI, CARGADOR\", ano: \"SE LE CAMBIO LA BATERÍA PORQUE YA NO TENIA ENERGIA, PERO YA NO ENCENDIÓ\", serie: \"VINO POR PAQUETERÍA\", nombreAseguradora: \"NO\", numeroEconomico: \"56 1915 9383\", numeroPolizaSeguro: \"4\"}\n  ) {\n    id\n    modelo\n    color\n    clienteId\n    placas\n    marca\n    motor\n    ano\n    serie\n    nombreAseguradora\n    numeroEconomico\n    numeroPolizaSeguro\n  }\n}"
    }
    response = requests.post(
        K_ENDPOING,
        json=payload,
        headers=headers,
    )
    
    
def save_os_to_kordata():
    currentToken = get_current_token()

    headers = {
        "user-agent": "pixel/0.0.1",
        "Content-Type": "application/json",
        "authorization": "Bearer " + currentToken,
    }
    payload = {
        "variables": {},
        "query": "mutation {\n  OrdenesServiciosGuardar(\n    data: {sucursalId: 1, almacenId: 1, clienteId: 5805, monedaId: 1, ordenesServiciosVehiculos: [{vehiculoId: 4403, isDeleted: false}], automotrizKms: \"Se le recomienda, no dejar el equipo apagado por mucho tiempo sin la batería\", campoAdicionalTexto2: \"Se le hizo un drenado de energia, se abrio el equipo para quitar la batería interna de reloj y la ram, se procedio a presionar el boton de encendido y se conectó el equipo, finalmente encendió, se hicieron pruebas de funcionamiento con y sin batería, el equipo funcionó bien\", nombreEntrego: \"Sin orden de compra\", ejecutivoId: 14880, comentarios: \"2\", impuestos: 0, descuento: 0, importeTotal: 0, subtotal: 0, ordenesServiciosDetalle: [{productoId: 3398, descripcion: \"MANO DE OBRA GARANTÍA\", precioUnitario: 0, cantidad: 2, impuestos: 0, tasasDocumentos: [], subtotal: 0, trazabilidadId: null, asesorServicioId: null, porcentajeDescuento: 0, horasTrabajo: 0, id: null, isDeleted: false}]}\n  ) {\n    id\n  }\n}"
    }
    response = requests.post(
        K_ENDPOING,
        json=payload,
        headers=headers,
    )