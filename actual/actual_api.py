import requests
from .data_model import CategoriesResponse

class ActualApi:
    def __init__(self, base_url: str, budget_sync_ID: str, actual_API_key: str):
        self.base_url = base_url
        self.budget_sync_ID = budget_sync_ID
        self.api_key=actual_API_key
        self.headers = {
            'accept': 'application/json',
            'x-api-key': self.api_key
        }

    def request(self, method: str, endpoint: str, params: dict = None) -> dict:
        """Fait une requête à l'API en fonction de la méthode spécifiée."""
        url = f"{self.base_url}/{self.budget_sync_ID}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=params)

        if response.status_code in [200, 201, 204]:
            # Pour les méthodes GET, POST et DELETE réussies
            if method.lower() == 'get':
                return response.json()
            else:
                return {'status': 'success'}
        else:
            print(f"Erreur : {response.status_code}")
            print(f"Message d'erreur : {response.text}")
            return {'status': 'error', 'message': response.text}

    def fetch_accounts(self):
        return self.request('get', 'accounts')

    def create_account(self, account_data: dict):
        return self.request('post', 'accounts', params=account_data)

    def delete_account(self, account_id: str):
        return self.request('delete', f'accounts/{account_id}')