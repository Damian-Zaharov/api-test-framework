from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    brand: str | None = None  # Поле может отсутствовать
    category: str
    thumbnail: str | None = None

class ProductListResponse(BaseModel):
    products: List[Product]
    total: int
    skip: int
    limit: int
