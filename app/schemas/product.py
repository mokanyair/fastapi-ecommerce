from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    


class ProductCreate(ProductBase):
   name: str = Field(..., min_length=2, max_length=100)
   description: Optional[str] = None
   price: float = Field(..., gt=0)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True  