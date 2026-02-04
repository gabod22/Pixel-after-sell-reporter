import os
import logging
import threading
import wsgiref.simple_server
import wsgiref.util
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from modules.Google.google_config import SCOPES
from googleapiclient.errors import HttpError

# A veces necesario para evitar errores de SSL en localhost
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from PySide6.QtCore import QObject, Signal
class AuthSignals(QObject):
    auth_success = Signal()
class GoogleContactsApi:
    def __init__(self,parent, token_path, creds_path):
        self.parent = parent
        self.token_path = token_path
        self.creds_path = creds_path
        self.creds_people = None
        self.auth_url = None

    def get_credentials(self, parent_gui=None):
        """Obtiene credenciales manejando el flujo manualmente para evitar CSRF."""
        creds = None

        # 1. Carga inicial de archivo
        if os.path.exists(self.token_path):
            try:
                if os.path.getsize(self.token_path) > 0:
                    creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
            except Exception:
                creds = None

        # 2. Validación y Refresh
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception:
                    creds = None

            # 3. Si no hay credenciales, iniciamos el flujo manual
            if not creds:
                flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, SCOPES)
                flow.redirect_uri = 'http://localhost:8080/'
                self.auth_url, _ = flow.authorization_url(prompt='consent')
                
                signals = AuthSignals()
                # Función interna para escuchar en el puerto 8080 sin regenerar estado
                def run_manual_server():
                    try:
                        self.creds_people = self._listen_for_auth_response(flow, 8080)
                        if self.creds_people:
                            signals.auth_success.emit()
                    except Exception as e:
                        logging.error(f"Error en servidor manual: {e}")
                        self.creds_people = None

                # Lanzamos el hilo
                auth_thread = threading.Thread(target=run_manual_server, daemon=True)
                auth_thread.start()
                print("Abre la siguiente URL en tu navegador para autenticarte:")
                print(self.auth_url)
                # Lanzamos la UI
                if self.parent:
                    from dialogs.GoogleLoing_dialog import GoogleLogin 
                    
                    dialog = GoogleLogin(self.parent, self.auth_url)
                    signals.auth_success.connect(dialog.accept)
                    dialog.exec()

                # Esperamos al usuario
                
                auth_thread.join()
                creds = self.creds_people

            # 4. Guardado seguro
            if creds:
                with open(self.token_path, "w") as token_file:
                    token_file.write(creds.to_json())
            else:
                logging.error("No se obtuvieron credenciales.")
                return None

        return creds

    def _listen_for_auth_response(self, flow, port):
        """
        Levanta un servidor WSGI simple para atrapar el código de autorización
        y canjearlo por el token, SIN regenerar el flujo.
        """
        wsgi_app = _RedirectWSGIApp()
        local_server = wsgiref.simple_server.make_server('localhost', port, wsgi_app)
        
        # Espera UNA sola petición (el redirect de Google)
        local_server.handle_request()
        
        # Una vez recibida la petición, extraemos la respuesta completa
        # (ej: http://localhost:8080/?state=...&code=...)
        auth_response = wsgi_app.last_request_uri
        
        # Cerramos el servidor para liberar el puerto
        local_server.server_close()
        
        if auth_response:
            # Canjeamos el código por el token usando el flujo YA EXISTENTE
            # Aquí es donde se valida que el 'state' sea el mismo.
            flow.fetch_token(authorization_response=auth_response)
            return flow.credentials
        else:
            return None



    def verify_connection(self):
        """Verifica que la conexión con la API de contactos funcione correctamente."""
        try:
            if not self.creds_people:
                self.creds_people = self.get_credentials()

            service = build("people", "v1", credentials=self.creds_people)
            service.people().connections().list(
                resourceName="people/me",
                pageSize=1,
                personFields="names",
            ).execute()
            
            logging.info("✅ Conexión exitosa con la API de Google Contacts.")
            return True

        except HttpError as err:
            logging.error(f"Error de conexión con Google Contacts: {err}")
            return False

        except Exception as e:
            logging.error(f"Error inesperado al verificar conexión: {e}")
            return False

    def register_contact(self, name, phone):
        """Registra un nuevo contacto en Google Contacts."""
        try:
            if not self.creds_people:
                self.creds_people = self.get_credentials()

            service = build("people", "v1", credentials=self.creds_people)
            service.people().createContact(
                body={
                    "names": [{"givenName": name}],
                    "phoneNumbers": [{"value": phone}],
                }
            ).execute()

            logging.info(f"Contacto '{name}' registrado correctamente.")
            return True

        except HttpError as err:
            logging.error(f"Error al registrar contacto: {err}")
            raise RuntimeError(f"Error HTTP al registrar contacto: {err}")

        except Exception as e:
            logging.error(f"Error inesperado al registrar contacto: {e}")
            raise RuntimeError(f"Error inesperado al registrar contacto: {e}")

# --- Clase auxiliar para manejar la petición HTTP ---
class _RedirectWSGIApp(object):
    def __init__(self):
        self.last_request_uri = None

    def __call__(self, environ, start_response):
        # Reconstruimos la URL completa que envió Google
        uri = wsgiref.util.request_uri(environ)
        # A veces oauthlib se queja si es http, forzamos https para el string de validación
        # (aunque en localhost suele permitir http si OAUTHLIB_INSECURE_TRANSPORT=1)
        self.last_request_uri = uri
        
        start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
        return [b'<html><body><h1>Autenticacion completa</h1><p>Puedes cerrar esta ventana y volver a la aplicacion.</p></body></html>']