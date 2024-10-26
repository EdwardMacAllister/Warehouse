from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    branch_id = Column(Integer, ForeignKey('branches.id'))

    def __repr__(self):
        return f"<Expense(amount={self.amount}, description={self.description})>"
