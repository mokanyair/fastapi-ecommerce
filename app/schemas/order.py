from typing import List, Optional
from pydantic import BaseModel, Field

class CartItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderCreate(BaseModel):
    session_id: str


class OrderOut(BaseModel):
    id: int
    session_id: str
    total_amount: float
    status: str

    class Config:
        from_attributes = True
