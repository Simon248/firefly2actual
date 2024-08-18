from pydantic import BaseModel,ValidationError
from typing import List, Optional




### CATEGORIE MODEL ###
class CategoryAttributes(BaseModel):
    created_at: str
    name: str

class Category(BaseModel):
    id: str
    attributes: CategoryAttributes

class CategoryResponse(BaseModel):
    data: List[Category]

### ACCOUNT MODEL ###
class AccountAttributes(BaseModel):
    created_at: str
    updated_at: str
    active: bool
    name: str
    type: str
    currency_code: str
    current_balance: str
    current_balance_date: str
    include_net_worth: bool

class Account(BaseModel):
    type: str
    id: str
    attributes: AccountAttributes

class AccountResponse(BaseModel):
    data: List[Account]


###TRANSACTION MODEL###
class TransactionDetail(BaseModel):
    user: str
    transaction_journal_id: str
    type: str
    date: str
    order: int
    currency_id: str
    currency_code: str
    currency_name: str
    currency_symbol: str
    currency_decimal_places: int
    foreign_currency_id: Optional[str]
    foreign_currency_code: Optional[str]
    foreign_currency_symbol: Optional[str]
    foreign_currency_decimal_places: Optional[int]
    amount: str
    foreign_amount: Optional[str]
    description: str
    source_id: str
    source_name: str
    source_iban: Optional[str]
    source_type: str
    destination_id: str
    destination_name: str
    destination_iban: Optional[str]
    destination_type: str
    budget_id: Optional[str]
    budget_name: Optional[str]
    category_id: Optional[str]  # Rendue optionnelle pour accepter None
    category_name: Optional[str]  # Rendue optionnelle pour accepter None
    bill_id: Optional[str]
    bill_name: Optional[str]
    reconciled: bool
    notes: Optional[str]
    tags: List[str]
    internal_reference: Optional[str]  # Rendue optionnelle pour accepter None
    external_id: Optional[str]
    original_source: Optional[str]
    recurrence_id: Optional[str]
    recurrence_total: Optional[int]
    recurrence_count: Optional[int]
    bunq_payment_id: Optional[str]
    external_url: Optional[str]
    import_hash_v2: str
    sepa_cc: Optional[str]
    sepa_ct_op: Optional[str]
    sepa_ct_id: Optional[str]
    sepa_db: Optional[str]
    sepa_country: Optional[str]
    sepa_ep: Optional[str]
    sepa_ci: Optional[str]
    sepa_batch_id: Optional[str]
    interest_date: Optional[str]
    book_date: Optional[str]
    process_date: Optional[str]
    due_date: Optional[str]
    payment_date: Optional[str]
    invoice_date: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    zoom_level: Optional[int]
    has_attachments: bool

class TransactionAttributes(BaseModel):
    created_at: str
    updated_at: str
    user: str
    group_title: Optional[str]
    transactions: List[TransactionDetail]

# class TransactionLink(BaseModel):
#     rel: Optional[str]  # Rendue optionnelle pour accepter les cas où elle est absente
#     uri: Optional[str]  # Rendue optionnelle pour accepter les cas où elle est absente

# class TransactionLinks(BaseModel):
#     self: str  # Champ 'self' est requis et ne doit pas être optionnel
#     links: Optional[TransactionLink]  # Ajouté pour couvrir les champs manquants

class Transaction(BaseModel):
    type: str
    id: str
    attributes: TransactionAttributes
    # links: Optional[TransactionLinks]  # Links peuvent être optionnels

class TransactionResponse(BaseModel):
    data: List[Transaction]

### API DATA MODEL ###
class APIData(BaseModel):
    accounts: AccountResponse
    categories: CategoryResponse

# Dictionnaire pour mapper les endpoints aux modèles correspondants
endpoint_to_model = {
    'accounts': AccountResponse,
    'categories': CategoryResponse,
    'transactions': TransactionResponse,
    # Ajoutez d'autres endpoints et leurs modèles correspondants
}
