from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PaymentRequest(BaseModel):
    order_id: int
    amount: float


@app.post("/pay")
def process_payment(request: PaymentRequest):
    # simple logic for now
    if request.amount < 1000:
        return {"status": "SUCCESS"}
    return {"status": "FAILED"}