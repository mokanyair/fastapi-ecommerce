from app.core.redis import redis_client
from app.db.session import SessionLocal
import requests

CART_PREFIX = "cart:session:"

from app.core.redis import redis_client

CART_PREFIX = "cart:session:"

def get_cart_key(session_id: str):
    return f"{CART_PREFIX}{session_id}"


def add_to_cart(session_id: str, product_id: int, quantity: int = 1):
    key = get_cart_key(session_id)

    redis_client.hincrby(key, product_id, quantity)

    redis_client.expire(key, 86400)

def get_cart(session_id: str):
    key = get_cart_key(session_id)

    items = redis_client.hgetall(key)

    return [
        {"product_id": int(pid), "quantity": int(qty)}
        for pid, qty in items.items()
    ]
    
def remove_from_cart(session_id: str, product_id: int):
    key = get_cart_key(session_id)

    redis_client.hdel(key, product_id)
    
def clear_cart(session_id: str):
    key = get_cart_key(session_id)

    redis_client.delete(key)   
    
def validate_product(product_id: int):
    response = requests.get(f"http://app:8000/api/products/{product_id}")
    
    if response.status_code != 200:
        raise Exception(f"Product {product_id} not found")
    return response.json()