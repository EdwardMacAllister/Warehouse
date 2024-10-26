from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))  # Assuming users table exists
    product_id = Column(Integer, ForeignKey('products.id'))  # Assuming products table exists
    quantity = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})>"
