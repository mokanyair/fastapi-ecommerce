from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.services import product_service
from app.api.deps import get_db, get_current_user
import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ProductOut])
def read_products(


    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return product_service.get_products(db)

@router.get("/{product_id}", response_model=ProductOut)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return product_service.get_product(db, product_id )
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")        
    return product

@router.post("/", response_model=ProductOut)
def create_product(
    product_in: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    print(" Route: create_product")
    return product_service.create_product(db, product_in)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    product_in: ProductUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    product = product_service.update_product(db, product_id, product_in)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/health")
def health_check():
    return {"status": "ok"}