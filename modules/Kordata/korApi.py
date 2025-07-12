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
        response.raise_for_status()
        return response.json()