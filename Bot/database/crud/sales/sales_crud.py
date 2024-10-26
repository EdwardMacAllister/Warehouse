from sqlalchemy.orm import Session
from Bot.database.models import Sale


def create_sale(db: Session, product_id: int, user_id: int, quantity: int, total_price: float):
    """Create a new sale."""
    new_sale = Sale(product_id=product_id, user_id=user_id, quantity=quantity, total_price=total_price)
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


def delete_sale(db: Session, sale_id: int) -> bool:
    """Delete a sale by ID."""
    sale = db.query(Sale).filter(Sale.id == sale_id).one_or_none()
    if sale:
        db.delete(sale)
        db.commit()
        return True
    return False


def list_sales(db: Session):
    """List all sales."""
    return db.query(Sale).all()
