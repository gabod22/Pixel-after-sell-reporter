import requests
from .auth import get_current_token

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

    # def get(self, endpoint, params=None):
    #     """
    #     Send a GET request to the specified endpoint with optional parameters.
    #     """
        
    #     response = requests.get(f"{self.base_url}/{endpoint}", params=params)
    #     response.raise_for_status()
    #     return response.json()

    def post(self, query=None):
        """
        Send a POST request to the specified endpoint with optional data.
        """
        response = requests.post(
            self.base_url,
            json=query,
            headers=self.headers,
        )
        status_code = response.status_code
        print(f"Response status code: {status_code}")
        if status_code == 401:
            print("Unauthorized access. Please check your token.")
            raise Exception("Unauthorized access. Please check your token.")
        elif status_code == 403:
            print("Forbidden access. You do not have permission to access this resource.")
            raise Exception("Forbidden access. You do not have permission to access this resource.")
        elif status_code == 500:
            response_json = response.json()
            print(response_json)
            if "messageError" in response_json:
                if response_json["messageError"] == "jwt-expiret":
                    print("La session ha expirado. Por favor, inicie sesión de nuevo.")
                    raise Exception("La session ha expirado. Por favor, inicie sesión de nuevo.")
                else:
                    print(f"Server error: {response_json['message']}")
                    raise Exception(f"Server error: {response_json['message']}")
            else:
                raise Exception("Error en el servidor.")
        
        response.raise_for_status()
        return response.json()