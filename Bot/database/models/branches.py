from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Branch(Base):
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)

    def __repr__(self):
        return f"<Branch(name={self.name}, location={self.location})>"
