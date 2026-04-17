from typing import List, Optional
from pydantic import BaseModel, Field

class CartItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderCreate(BaseModel):
    user_id: int = Field(..., gt=0)


class OrderOut(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str

    class Config:
        from_attributes = True
