from sqlalchemy.orm import Session
from Bot.database.models import Supplier


def create_supplier(db: Session, name: str, contact_info: str):
    """Create a new supplier."""
    new_supplier = Supplier(name=name, contact_info=contact_info)
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier


def delete_supplier(db: Session, supplier_id: int) -> bool:
    """Delete a supplier by ID."""
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).one_or_none()
    if supplier:
        db.delete(supplier)
        db.commit()
        return True
    return False


def list_suppliers(db: Session):
    """List all suppliers."""
    return db.query(Supplier).all()
