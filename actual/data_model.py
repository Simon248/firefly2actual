from pydantic import BaseModel
from typing import List, Optional

from pydantic import BaseModel
from typing import List

class Category(BaseModel):
    id: str
    name: str
    is_income: bool
    hidden: bool
    group_id: str

class CategoriesResponse(BaseModel):
    data: List[Category]
