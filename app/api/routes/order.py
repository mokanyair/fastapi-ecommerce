from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_services import create_order


router = APIRouter()

@router.post("/", response_model=OrderOut)
def create_order_endpoint(
    order_in: OrderCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_order(db, order_in.user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))