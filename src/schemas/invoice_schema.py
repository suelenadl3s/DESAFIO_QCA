from pydantic import BaseModel
from typing import List

class ProductSchema(BaseModel):
    name: str
    price: float
    quantity: int


class InvoiceSchema(BaseModel):
    order_id: str
    date: str
    customer_id: str
    products: List[ProductSchema]