import json
import logging
from pathlib import Path
from typing import List, Union, Optional

import gspread
import requests
import google.auth.exceptions
from gspread import Worksheet
from gspread.exceptions import (
    SpreadsheetNotFound, WorksheetNotFound, APIError,
)

from modules.Google.google_config import (
    gspread_file,
    GOOGLE_SHEET_NAME,
    GOOGLE_WOTKSHEET_ID,
)
from google.oauth2.service_account import Credentials

LETTERS = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]


class WorksheetApi():
    def __init__(self, worksheet: Worksheet):
        self.worksheet = worksheet

    def write_cell(self, value: str, note: str, row: int, col: int):
        logging.debug(f"Escribiendo en celda {LETTERS[col]}{row}: {value}")
        self.worksheet.update_cell(row, col, value)
        if note:
            self.worksheet.insert_note(f"{LETTERS[col]}{row}", note)

    def write_range(self, data: List[List[str]], row: int, col: str):
        cell_range = f"{col}{row}"
        logging.debug(f"Escribiendo rango en {cell_range}")
        self.worksheet.update(cell_range, data)

    def ensure_enough_rows(self, min_required_rows: int):
        current_rows = self.worksheet.row_count
        if current_rows < min_required_rows:
            rows_to_add = min_required_rows - current_rows
            logging.info(f"Agregando {rows_to_add} filas a la hoja (de {current_rows} a {min_required_rows})")
            self.worksheet.add_rows(rows_to_add)

    def write_in_last_row(self, data: List[List[str]]):
        values_list = self.worksheet.col_values(1)
        new_row_index = len(values_list)
        target_row = new_row_index + 1

        # Asegura que la hoja tenga al menos esa fila
        self.ensure_enough_rows(target_row)

        # Insertar el índice como primer valor en la fila
        # data[0].insert(0, new_row_index)

        cell_start = f"A{target_row}"
        logging.debug(f"Escribiendo en última fila {cell_start}")
        self.worksheet.update(cell_start, data, value_input_option="USER_ENTERED")

    def insert_notes(self, notes: List[str], row: int):
        for i, note in enumerate(notes):
            if note:
                cell = f"{LETTERS[i]}{row}"
                logging.debug(f"Insertando nota en {cell}: {note}")
                self.worksheet.insert_note(cell, note)

    def find_row_by_value(self, value: str, column: int) -> int:
        logging.info(f"Buscando valor '{value}' en columna {column}")
        try:
            cell = self.worksheet.find(value, in_column=column)
            if cell:
                logging.debug(f"Encontrado en fila: {cell.row}")
                return cell.row
        except Exception as e:
            logging.warning(f"No se encontró el valor '{value}': {e}")
        return -1


    
    
class GoogleSpreadsheetApi:
    def __init__(self):
        logging.debug("Inicializando instancia de GoogleSpreadsheetApi")

    def get_worksheet(self) -> WorksheetApi:
        logging.info("Obteniendo worksheet...")

        worksheet = self.get_spreadsheet(
            gspread_file, GOOGLE_WOTKSHEET_ID, GOOGLE_SHEET_NAME
        )
        return WorksheetApi(worksheet)

    def get_email(self):
        creds = Credentials.from_service_account_file(str(gspread_file))
        logging.info(f"Service account email: {creds.service_account_email}")
            

    def get_credentials(
        self,
        input_credentials: Union[str, Path],
    ) -> dict:
        """
        Devuelve las credenciales de un archivo JSON o cadena JSON.
        """
        path = Path(input_credentials)

        try:
            if path.is_file():
                logging.debug(f"Cargando credenciales desde archivo: {path}")
                return json.loads(path.read_text(encoding="utf-8"))
            else:
                logging.debug("Cargando credenciales desde cadena JSON")
                return json.loads(str(input_credentials))
        except Exception as e:
            logging.error(f"Error al cargar credenciales: {e}")
            raise ValueError("No se pudo leer el JSON de la cuenta de servicio.")

    def get_spreadsheet(
        self,
        json_file: Union[str, Path],
        doc_id: str,
        worksheet_name: str,
    ) -> Worksheet:
        """
        Retorna un Worksheet de gspread basado en las credenciales y nombres indicados.
        """
        logging.info(f"Accediendo a hoja de cálculo {doc_id}, hoja: {worksheet_name}")
        credentials = self.get_credentials(json_file)
        gspread_client = gspread.service_account(filename=str(json_file))
        logging.debug(f"Google spread client initialised: {gspread_client}")
        try:
            sheet = gspread_client.open_by_key(doc_id)
            logging.debug(f"Título del archivo: {sheet.title}")

            # Intenta obtener la hoja
            ws = sheet.worksheet(worksheet_name)
            logging.debug(f"Título de la hoja encontrada: {ws.title}")
            return ws
        # except PermissionError:
        #     logging.exception('No tienes permiso para acceder a este worksheet')
        #     raise Exception('No tienes permiso para acceder a este worksheet')
        
        except SpreadsheetNotFound:
            logging.exception("Hoja de cálculo no encontrada o inaccesible.")
            raise Exception("No se encontró el documento de hoja de cálculo.")
        
        except WorksheetNotFound:
            logging.exception("Hoja específica no encontrada.")
            raise Exception(f"La hoja '{worksheet_name}' no existe.")
        
        except google.auth.exceptions.RefreshError:
            logging.exception("Desincronización de hora en sistema.")
            raise Exception("Sincroniza la hora del equipo con la hora del servidor.")
        
        except requests.exceptions.ConnectionError:
            logging.exception("Error de conexión.")
            raise Exception("Conexión cerrada sin respuesta. Intente de nuevo.")
        
        except APIError as e:
            logging.exception("APIError al acceder a Google Sheets.")
            if hasattr(e, "response"):
                error_json = e.response.json()
                error_status = error_json.get("error", {}).get("status")
                error_message = error_json.get("error", {}).get("message", "")
                email = credentials.get("client_email", "(email missing)")

                if error_status == "INVALID_ARGUMENT":
                    raise Exception(f"Error de argumento inválido: {error_message}")
                elif error_status == "PERMISSION_DENIED":
                    raise Exception(
                        f"Permiso denegado: {error_message}. "
                        f"¿Compartiste la hoja con {email} y habilitaste la API?"
                    )
                elif error_status == "NOT_FOUND":
                    raise Exception(
                        f"Documento no encontrado. Verifica el ID: {doc_id}"
                    )
            raise Exception(f"Error de la API de Google: {e}")


