from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    contact_info = Column(String)

    def __repr__(self):
        return f"<Supplier(name={self.name}, contact_info={self.contact_info})>"
