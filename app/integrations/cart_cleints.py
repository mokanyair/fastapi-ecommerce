import requests
from typing import Dict, Any


CART_URL = "http://app:8000/api/v1/cart"


def get_cart(session_id: str) -> Dict[str, Any]:
    response = requests.get(f"{CART_URL}?session_id={session_id}")

    if response.status_code != 200:
        raise Exception("Failed to fetch cart")
    
    print("Fetching cart for session:", session_id)
    print("Cart response:", response.json())

    return response.json()
   