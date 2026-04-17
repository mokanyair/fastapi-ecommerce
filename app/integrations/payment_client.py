import requests
from typing import Dict


PAYMENT_URL = "http://payment-service:8000/pay"


def process_payment(order_id: int, amount: float) -> Dict:
    response = requests.post(
        PAYMENT_URL,
        json={"order_id": order_id, "amount": amount},
        timeout=5,
    )

    if response.status_code != 200:
        return {"status": "FAILED"}

    return response.json()