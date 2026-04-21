import requests

PRODUCT_URL = "http://app:8000/api/v1/products"

def get_product(product_id: int):
    response = requests.get(f"{PRODUCT_URL}/{product_id}")

    if response.status_code != 200:
        raise Exception(f"Product {product_id} not found")

    return response.json()

def validate_product(product_id: int):
    response = requests.get(f"{PRODUCT_URL}/{product_id}")
    return response.status_code == 200

