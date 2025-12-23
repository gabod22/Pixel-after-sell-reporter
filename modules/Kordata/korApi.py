import ssl
import requests
from .auth import get_current_token
from .kordataConfig import kordata_chain  # ya no se usará, pero lo dejo por si luego quieres volver a CA bundle
import certifi

class KordataApi:
    """
    Kordata API class for handling API requests and responses.
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.currentToken = get_current_token()
        self.headers = {
            "user-agent": "pixel/0.0.1",
            "Content-Type": "application/json",
            "authorization": "Bearer " + self.currentToken,
        }

        # Crear contexto SSL cifrado pero sin validación estricta del certificado
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    def post(self, query=None):
        """
        Send a POST request to the specified endpoint with optional data.
        """
        response = requests.post(
            self.base_url,
            json=query,
            headers=self.headers,
            verify=False  # Importante: dejamos verify=False para que no choque con el contexto
        )

        status_code = response.status_code
        print(f"Response status code: {status_code}")

        if status_code == 401:
            raise Exception("Unauthorized access. Please check your token.")
        elif status_code == 403:
            raise Exception("Forbidden access.")
        elif status_code == 500:
            response_json = response.json()
            if "messageError" in response_json:
                if response_json["messageError"] == "jwt-expiret":
                    raise Exception("La sesión ha expirado. Inicie sesión nuevamente.")
                else:
                    raise Exception(f"Server error: {response_json['messageError']}")
            else:
                raise Exception("Internal server error.")
        
        response.raise_for_status()
        return response.json()
