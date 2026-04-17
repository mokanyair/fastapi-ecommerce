import requests

PRODUCT_URL = "http://product-service:8000/api/v1/products"

def validate_product(product_id: int):
    response = requests.get(f"{PRODUCT_URL}/{product_id}")
    return response.status_code == 200

