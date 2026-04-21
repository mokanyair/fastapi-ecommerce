from sqlalchemy.orm import Session
from app.models.order import Order

def create_order(db: Session, session_id: str, total_amount: float) -> Order:
    order = Order(
        session_id=session_id,
        total_amount=total_amount,
        status="PENDING",
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def update_order_status(db: Session, order: Order, status: str) -> Order:
    order.status = status
    db.commit()
    db.refresh(order)
    return order