import datetime
from globals import getConfig
config = getConfig()
date = datetime.datetime.strptime(config["KORDATA"]['START_DATE'], "%d/%m/%Y")
START_DATE = date.strftime("%Y-%m-%d")
K_ENDPOING = "https://biz3.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one3.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one3.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one3.kordata.mx/api/commons/cerrar-sesion-masivo"

sell_notes_columns = [
    "Folio",
    "Sucursal",
    "Nombre del cliente",
    "Fecha registro",
    "Estado",
    "Subtotal",
    "Descuento",
    "Impuestos",
    "Importe del total",
    "Vendedor",
]
items_cols = [
    "SKU",
    "Descripcion",
    "Cantidad",
    "Precio unitario",
    "Impuestos",
    "Porcentaje de descuento",
    "Subtotal",
    "Importe",
]

print(START_DATE)