from asyncio.log import logger
from http.client import HTTPException

from sqlalchemy.orm import Session
from app.crud.product import product_crud
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(db: Session):
    return product_crud.get_multi(db)


def get_product(db: Session, product_id: int):
    logger.info(f"Fetching product {product_id}")
    
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product    
  


def create_product(db: Session, product_in: ProductCreate):
    print(" Service: create_product")
    return product_crud.create(db, product_in)


def update_product(db: Session, product_id: int, product_in: ProductUpdate):
    db_obj = product_crud.get(db, product_id)
    if not db_obj:
        return None
    return product_crud.update(db, db_obj, product_in)