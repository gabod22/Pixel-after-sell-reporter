import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/contacts"]


class GoogleContactsApi:
    def __init__(self, token_path, creds_path):
        self.token_path = token_path
        self.creds_path = creds_path
        self.creds_people = None

    def get_credentials(self):
        """Obtiene o refresca las credenciales de Google Contacts."""
        creds = None

        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, SCOPES)
                creds = flow.run_local_server(port=0, open_browser=False)

            with open(self.token_path, "w") as token_file:
                token_file.write(creds.to_json())

        return creds

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

            print("✅ Conexión exitosa con la API de Google Contacts.")
            return True

        except HttpError as err:
            print(f"❌ Error de conexión con Google Contacts: {err}")
            return False

        except Exception as e:
            print(f"❌ Error inesperado al verificar conexión: {e}")
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

            print(f"✅ Contacto '{name}' registrado correctamente.")
            return True

        except HttpError as err:
            raise RuntimeError(f"Error HTTP al registrar contacto: {err}")

        except Exception as e:
            raise RuntimeError(f"Error inesperado al registrar contacto: {e}")
