import requests
from typing import Dict, Type

class FireflyAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
        self.headers = {
            'accept': 'application/vnd.api+json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def fetch_data(self, endpoint: str, params: dict = None) -> dict:
        """Fait une requête à l'API et gère la pagination."""
        all_data = []
        url = f"{self.base_url}/{endpoint}"
        while url:
            response = requests.get(url, headers=self.headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                all_data.extend(data.get('data', []))  # Ajouter les données de la page actuelle
                url = data['links'].get('next')  # Mettre à jour l'URL pour la page suivante
            else:
                print(f"Erreur : {response.status_code}")
                break
        
        return {'data': all_data}