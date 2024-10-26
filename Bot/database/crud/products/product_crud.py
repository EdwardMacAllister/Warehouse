from sqlalchemy.orm import Session
from sqlalchemy import select
from Bot.database.models.products import Product


def create_product(db: Session, name: str, price: float, quantity: int):
    new_product = Product(name=name, price=price, quantity=quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def delete_product(db: Session, product_id: int):
    product = db.execute(select(Product).where(Product.id == product_id)).scalar_one_or_none()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False


def list_products(db: Session):
    return db.execute(select(Product)).scalars().all()
