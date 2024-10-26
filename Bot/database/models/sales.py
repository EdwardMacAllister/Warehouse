from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))  # Assuming there's a Product model
    user_id = Column(Integer, ForeignKey('users.id'))  # Assuming there's a User model
    quantity = Column(Integer)
    total_price = Column(Float)
    sale_date = Column(DateTime)
    branch_id = Column(Integer, ForeignKey('branch.id'))

    def __repr__(self):
        return f"<Sale(product_id={self.product_id}, user_id={self.user_id}, quantity={self.quantity}, total_price={self.total_price})>"
