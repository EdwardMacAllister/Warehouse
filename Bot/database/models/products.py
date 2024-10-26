from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, quantity={self.quantity})>"
