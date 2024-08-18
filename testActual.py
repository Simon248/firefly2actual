from actual.actual_api import ActualApi
from pydantic import BaseModel,ValidationError

import json

from secrets import actual_base_url , actual_budget_sync_ID , actual_API_key

# Actual_Base_url = 'http://localhost:5007/v1/budgets'
# budget_sync_ID='actual_budget_sync_ID'
# api_key_file='actual_API_key'

Api=ActualApi(base_url=actual_base_url,budget_sync_ID=actual_budget_sync_ID,actual_API_key=actual_API_key)
print(Api.fetch_accounts())
param = {
'account': {
    'name': 'Checking',
    'offbudget': False
}
}
# print(Api.create_account(param))
print(Api.delete_account('bde99354-9ffd-47b8-b920-a856dffa155a'))
print(Api.fetch_accounts())
# A=Api.fetch_data('categories')
# print(A)
# print(type(A))

