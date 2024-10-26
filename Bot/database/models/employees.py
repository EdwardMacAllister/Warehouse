from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    branch_id = Column(Integer, ForeignKey('branches.id'))  # Assuming this is a foreign key to a Branch
    position = Column(Integer, ForeignKey('position.id'))

    def __repr__(self):
        return f"<Employee(name={self.name}, branch_id={self.branch_id})>"
