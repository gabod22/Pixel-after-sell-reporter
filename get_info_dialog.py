from PySide6.QtWidgets import (
    QDialog,
)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt
from ui.get_info_dialog_ui import Ui_GetInfoDialog

# from tabulate import tabulate

import sys
import pandas as pd
from os import path

from dialogs import showSuccessDialog, showFailDialog, show_yes_no_dialog
from helpers import get_current_token
from login_dialog import LoginDialog

import requests
import time
import json
import pickle


# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable), '_internal')
elif __file__:
    dirname = path.join(path.dirname(__file__))

USERNAME = "consultoria@pixel-lap.com"
PASS = "P0nk3h4k13224"

START_DATE = "2022-01-01"

K_ENDPOING = "https://biz.kordata.mx/graphql"
K_LOGIN_ENDPOINT = "https://one.kordata.mx/api/commons/iniciar-sesion"
K_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion"
K_MASIVE_LOGOUT_ENDPOINT = "https://one.kordata.mx/api/commons/cerrar-sesion-masivo"


class GetInfoDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_GetInfoDialog()
        self.ui.setupUi(self)
        try:
            self.join_notes_and_items()
        except:
            print('No se pudo obtener la info debido a tal')
            self.parent.show_login_dialog()
        finally:
            self.close()



    
    def get_sales_invoices(self):
        currentToken = get_current_token()

        headers = {
            "user-agent": "pixel/0.0.1",
            "Content-Type": "application/json",
            "authorization": "Bearer " + currentToken,
        }
        query_report_list_invoices = {
            "operationName": "some",
            "variables": {},
            "query": 'query some {\n  BasesReportesGenerarReportePorId(\n    data: {id: 100000105}\n    parametros: {columnasAdicionales: [{id: -1, baseCampoId: 2471, seLect: false, wheRe: true, groUp: false, baseReporteCondicionCatalogoId: 25, groupAscendente: null, andOr: "AND", visible: true, esId: false, isDeleted: false, secuencia: -1, baseReporteId: 100000105}], condicionesAdicionales: [{valorInicial: "'
            + START_DATE
            + '", valorFinal: "", baseReporteColumnaId: -1}]}\n  ) {\n    datosListasSeleccion\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      carpetaId\n      parasiteParent\n      compartida\n      esQuery\n      nombreReporte\n      tablaPrincipalId\n      moduloPrincipalId\n      baseReporteTipoId\n      baseReporteIdDetalle\n      basesReportesColumnas {\n        id\n        basesCampos {\n          nombreEtiqueta\n        }\n      }\n      basesReportesPivotConfiguracion {\n        baseReporteColumnaId\n        baseCampoAlias\n        pivotColumna\n        pivotRenglon\n        pivotValor\n      }\n    }\n  }\n}',
        }
        response = requests.post(
            K_ENDPOING,
            json=query_report_list_invoices,
            headers=headers,
        )
        invoices = response.json()["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["encabezado"]
        invoices.pop(0)
        items = response.json()["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["detalle"]
        items.pop(0)

        # print(type(data))
        return invoices, items

    # @mide_tiempo
    def get_sales_notes(self):
        try:
            
            currentToken = get_current_token()
            headers = {
                "user-agent": "pixel/0.0.1",
                "Content-Type": "application/json",
                "authorization": "Bearer " + currentToken,
            }
            query_report_list_sales_notes = {
                "operationName": "some",
                "variables": {},
                "query": 'query some {\n  BasesReportesGenerarReportePorId(\n    data: {id: 100000104}\n    parametros: {columnasAdicionales: [{id: -1, baseCampoId: 2519, seLect: false, wheRe: true, groUp: false, baseReporteCondicionCatalogoId: 25, groupAscendente: null, andOr: "AND", visible: true, esId: false, isDeleted: false, secuencia: -1, baseReporteId: 100000104}], condicionesAdicionales: [{valorInicial: "'
                + START_DATE
                + '", valorFinal: "", baseReporteColumnaId: -1}]}\n  ) {\n    datosListasSeleccion\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      carpetaId\n      parasiteParent\n      compartida\n      esQuery\n      nombreReporte\n      tablaPrincipalId\n      moduloPrincipalId\n      baseReporteTipoId\n      baseReporteIdDetalle\n      basesReportesColumnas {\n        id\n        basesCampos {\n          nombreEtiqueta\n        }\n      }\n      basesReportesPivotConfiguracion {\n        baseReporteColumnaId\n        baseCampoAlias\n        pivotColumna\n        pivotRenglon\n        pivotValor\n      }\n    }\n  }\n}',
            }
            response = requests.post(
                K_ENDPOING,
                json=query_report_list_sales_notes,
                headers=headers,
            )
            sales_notes = response.json()["data"]["BasesReportesGenerarReportePorId"][
                "resultadoReporteHashmap"
            ][0]["encabezado"]
            sales_notes.pop(0)
            items = response.json()["data"]["BasesReportesGenerarReportePorId"][
                "resultadoReporteHashmap"
            ][0]["detalle"]
            items.pop(0)

            # print(type(data))
            return sales_notes, items
        except:
            pass
        

    def get_clients(self):
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

            return clients
        except:
            pass
    
    def join_notes_and_items(self):
        sales_notes, sales_notes_items = self.get_sales_notes()
        invoices, invoices_items = self.get_sales_invoices()
        clients = self.get_clients()
        # print(clients)
        
        for note in sales_notes:
            # Filtrar elementos de array2 que coincidan en id
            note["items"] = [sub_item for sub_item in sales_notes_items if sub_item["id"] == note["id"]]
        
        for note in sales_notes:
            phones = [client['Teléfono'] for client in clients if client["Nombre del cliente"] == note["Cliente - Nombre del cliente"]]
            phone_r = None
            if phones:
                for phone in phones:
                    if phone != "" and type(phone) == str:
                        phone_r = phone
                        break
            note["phone"] = phone_r
            
            
        for invoice in invoices:
            # Filtrar elementos de array2 que coincidan en id
            invoice["items"] = [sub_item for sub_item in invoices_items if sub_item["id"] == invoice["id"]]
        
        for invoice in invoices:
            phones = [client['Teléfono'] for client in clients if client["Nombre del cliente"] == invoice["Cliente - Nombre del cliente"]]
            phone_r = None
            if phones:
                for phone in phones:
                    if phone != "" and type(phone) == str:
                        phone_r = phone
                        break
            invoice["phone"] = phone_r
            
        data = invoices + sales_notes
        
        search_info = self.dictlist_to_str_list(data, ['Folio', 'Cliente - Nombre del cliente', 'phone', 'Fecha registro'])
        # print(data)
        data_hash = {}
        
        for d in data:
            data_hash[d['Folio']] = d
            
        json_object = json.dumps(data_hash, indent=4)
        
        self.save_info(data_hash,search_info)
        
    def save_info(self, data_hash, array):
        try:
            
            with open(path.join(dirname,"sells.pkl"), "wb") as file:
                pickle.dump(data_hash, file)
            with open(path.join(dirname,'search_data.pkl'), 'wb') as file:
                pickle.dump(array,file)

            showSuccessDialog(self,"Se actualizó la información correctamente")
            self.parent.load_info()
            self.close()
            
        except Exception as e:
            showFailDialog(self,"Ocurrió un error, revise que haya seleccionado los archivos correctos o que los exportó correctamente")
            print(e)
    def update_info(self):
        pass
    def logout(self,token):
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
        
    
    def dictlist_to_str_list(self,list, cols):
        result = []
        for row in list:
            text = ""
            for (i, col) in enumerate(cols):
                value = row[col] if row[col] != None else ""
                text = text + str(value)
                
                if i < len(cols)-1:
                    text = text + " - "
            text = text.replace("\n", "").replace("\r", "").strip()
            result.append(text)
        return result
    