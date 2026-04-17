from fastapi import FastAPI
from fastapi import FastAPI
from app.api.routes import cart, products, order
from app.db.init_db import init_db
import logging

logging.logging.disable(logging.CRITICAL)

app = FastAPI()

# create tables
init_db()

app.include_router(products.router, prefix="/api/v1/products", tags=["products"])

app.include_router(cart.router, prefix="/api/v1/cart", tags=["cart"])

app.include_router(order.router, prefix="/orders", tags=["orders"])

