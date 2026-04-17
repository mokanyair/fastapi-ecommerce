from fastapi import APIRouter, Depends, HTTPException
from app.services import cart_service

router = APIRouter()

@router.post("/add")
def add_to_cart(
    session_id: str,
    product_id: int,
    quantity: int = 1
):
    cart_service.add_to_cart(session_id, product_id, quantity)
    return {"message": "Product added to cart"}

@router.get("/")
def get_cart(session_id: str):
    cart = cart_service.get_cart(session_id)
    return {"cart": cart} 

@router.post("/remove")
def remove_from_cart(
    session_id: str,
    product_id: int
):
    cart_service.remove_from_cart(session_id, product_id)
    return {"message": "Product removed from cart"} 