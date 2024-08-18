from pydantic import BaseModel,ValidationError
from firefly.firefly_api import FireflyAPI
from firefly.populate_model import PopulateModel
import json

from secrets import firefly_base_url , firefly_PAT

# Initialisation de la classe PopulateModel
populate_model = PopulateModel(base_url=firefly_base_url, token=firefly_PAT)

# Récupération de toutes les données    
# TODO, cette méthode pourrait etre appelée à l'instanciation de la classe PopulateModel
all_data = populate_model.fetch_all_model_data()

print(all_data.categories.model_dump())

# data=populate_model.fetch_data(f'accounts/185/transactions')
# print(json.dumps(data))