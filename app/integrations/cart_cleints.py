import requests
from typing import Dict, Any


CART_URL = "http://cart-service:8000/api/v1/cart"


def get_cart(user_id: int) -> Dict[str, Any]:
    response = requests.get(f"{CART_URL}?user_id={user_id}")

    if response.status_code != 200:
        raise Exception("Failed to fetch cart")

    return response.json()