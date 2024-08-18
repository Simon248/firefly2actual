from pydantic import BaseModel
from . import pydantic_data_model as data_model
from pydantic import BaseModel
from typing import Dict, Type
from . import firefly_api


class PopulateModel(firefly_api.FireflyAPI):
    def __init__(self, base_url: str, token: str):
        # Initialiser la classe parente (FireflyAPI)
        super().__init__(base_url, token)


    def parse_data_to_model(self,data: dict, model_class: Type[BaseModel]) -> BaseModel:
        """Valide et structure les données avec Pydantic."""
        return model_class(**data)

    def fetch_all_model_data(self, endpoint_to_model: Dict[str, Type[BaseModel]]= data_model.endpoint_to_model) -> BaseModel:
        """Récupère les données de plusieurs endpoints et les structure en utilisant Pydantic."""
        results = {}

        # Récupération et structuration des données des comptes
        accounts_data = self.fetch_data('accounts')
        accounts = self.parse_data_to_model(accounts_data, endpoint_to_model['accounts'])
        results['accounts'] = accounts

        # Filtrer les comptes de type "asset"
        asset_accounts = [account for account in accounts.data if account.attributes.type == "asset"]

        # Récupérer les transactions pour chaque compte "asset"
        transactions = []
        for account in asset_accounts:
            print(account.id)
            account_transactions = self.fetch_data(f'accounts/{account.id}/transactions')
            transactions.extend(account_transactions['data'])  # Ajouter les transactions à la liste globale

        # Structurer les transactions dans un modèle Pydantic
        transactions_data = {'data': transactions}
        results['transactions'] = self.parse_data_to_model(transactions_data, endpoint_to_model['transactions'])

        # recupérer les categories
        categories_data = self.fetch_data('categories')
        categories = self.parse_data_to_model(categories_data, endpoint_to_model['categories'])
        results['categories'] = categories

        return data_model.APIData(**results)

        

        # for endpoint, model in endpoint_to_model.items():
        #     raw_data = self.fetch_data(endpoint)

        #     structured_data = self.parse_data_to_model(raw_data, model)
        #     print("youpi")
        #     results[endpoint] = structured_data
        
        # return data_model.APIData(**results)