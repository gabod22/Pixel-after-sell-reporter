import datetime
from os import path
from globals import getConfig

from globals import dirname
config = getConfig()
date = datetime.datetime.strptime(config["KORDATA"]['START_DATE'], "%d/%m/%Y")
START_DATE = date.strftime("%Y-%m-%d")
K_ENDPOING = "https://biz.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion-masivo"

import logging

kordata_chain = path.join(dirname, "kordata_chain.crt")
logging.info(f"Ruta CA: {kordata_chain}, Existe el archivo?: {path.exists(kordata_chain)}")


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
logging.debug(f"START_DATE used in kordata app is: {START_DATE}")