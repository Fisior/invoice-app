from typing import List
from pydantic import BaseModel


class CustomerSchema(BaseModel):
    id: int
    name: str
    email: str


class InvoiceSchema(BaseModel):
    id: int
    amount: float
    date: str
    customer_id: int