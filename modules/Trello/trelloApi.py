import requests
from .trelloConfig import TRELLO_ID_LIST, TRELLO_KEY, TRELLO_TOKEN, TRELLO_ENDPOINT, TRELLO_HEADERS
from .trelloConfig import trello_labels, trello_members

class TrelloApi:
    def __init__(self):
        self.base_url = TRELLO_ENDPOINT
        self.api_key = TRELLO_KEY
        self.token = TRELLO_TOKEN
        self.headers = TRELLO_HEADERS
        self.trello_list = TRELLO_ID_LIST
        
    def add_card(self, cardName, desc, labels, members):
        """_summary_

        Args:
            cardName (_type_): Nombre de la tarjeta a crear.
            desc (_type_): descripción de la tarjeta.
            labels (_type_): Diccionario de etiquetas donde las claves son los nombres de las etiquetas y los valores son sus IDs.
            members (_type_): mapeo de miembros donde las claves son los nombres de los miembros y los valores son sus IDs.

       
        Returns:
            string: Es la URL corta de la tarjeta creada en Trello.
        """
        query = {
            "idList": self.trello_list,
            "key": self.api_key,
            "token": self.token,
            "name": cardName,
            "desc": desc,
            "idLabels": [trello_labels[label] for label in labels],
            "idMembers": [trello_members[member] for member in members],
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                params=query,
                timeout=10  # Opcional: evita cuelgues por red lenta
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error de conexión con Trello: {e}")

        # Manejo de errores por código de estado HTTP
        if response.status_code == 200:
            data = response.json()
            short_url = data.get("shortUrl")
            if not short_url:
                raise RuntimeError("No se recibió un enlace de tarjeta válido desde Trello.")
            return short_url

        elif response.status_code == 400:
            raise RuntimeError("Solicitud incorrecta (400). Verifica los datos enviados.")

        elif response.status_code == 401:
            raise RuntimeError("No autorizado (401). Verifica tu token y API key de Trello.")

        elif response.status_code == 403:
            raise RuntimeError("Prohibido (403). No tienes permisos para agregar tarjetas en este tablero.")

        elif response.status_code == 404:
            raise RuntimeError("Recurso no encontrado (404). Revisa la URL o el ID del tablero.")

        elif response.status_code >= 500:
            raise RuntimeError("Error del servidor de Trello. Intenta más tarde.")

        else:
            raise RuntimeError(f"Error inesperado ({response.status_code}): {response.text}")

    def get_boards(self):
        url = f"{self.base_url}/members/me/boards"
        params = {
            "key": self.api_key,
            "token": self.token,
            "fields": "name,id"
        }
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None

    def get_board_lists(self, board_id):
        url = f"{self.base_url}/boards/{board_id}/lists"
        params = {
            "key": self.api_key,
            "token": self.token,
            "fields": "name,id"
        }
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None