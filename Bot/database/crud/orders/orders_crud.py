from sqlalchemy.orm import Session
from sqlalchemy import select
from Bot.database.models.orders import Order


def create_order(db: Session, product_id: int, user_id: int, quantity: int, total_price: float):
    """Create a new order."""
    new_order = Order(product_id=product_id, user_id=user_id, quantity=quantity, total_price=total_price)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def get_order_by_id(db: Session, order_id: int):
    """Get an order by ID."""
    return db.execute(select(Order).where(Order.id == order_id)).scalar_one_or_none()


def delete_order(db: Session, order_id: int) -> bool:
    """Delete an order by ID."""
    order = db.execute(select(Order).where(Order.id == order_id)).scalar_one_or_none()
    if order:
        db.delete(order)
        db.commit()
        return True
    return False


def list_orders(db: Session):
    """List all orders."""
    return db.execute(select(Order)).scalars().all()


def update_order(db: Session, order_id: int, quantity: int = None, total_price: float = None):
    """Update an existing order."""
    order = db.execute(select(Order).where(Order.id == order_id)).scalar_one_or_none()
    if order:
        if quantity is not None:
            order.quantity = quantity
        if total_price is not None:
            order.total_price = total_price
        db.commit()
        return order
    return None
