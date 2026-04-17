import logging
from sqlalchemy.orm import Session
from app.crud import crud_order
from app.integrations.cart_cleints import get_cart
#from app.integrations.payment_client import process_payment
from app.integrations.event_bus import publish_event
from app.integrations.payment_client import process_payment

logger = logging.getLogger(__name__)


def create_order(db: Session, user_id: int):
    logger.info(f"Creating order for user {user_id}")

    # 1. Fetch cart
    cart = get_cart(user_id)

    items = cart.get("items", [])
    if not items:
        raise ValueError("Cart is empty")

    # 2. Calculate total
    total_amount = sum(
        item["price"] * item["quantity"] for item in items
    )

    # 3. Create order
    order = crud_order.create_order(db, user_id, total_amount)

    # 4. Process payment
    payment_result = process_payment(order.id, total_amount)

    if payment_result.get("status") == "SUCCESS":
        order = crud_order.update_order_status(db, order, "PAID")

        # 5. Publish event
        publish_event(
            "order_paid",
             {
                 "order_id": order.id,
                 "items": items,
             },
         )
    else:
        order = crud_order.update_order_status(db, order, "FAILED")

    return order