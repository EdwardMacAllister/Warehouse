from sqlalchemy.orm import Session
from Bot.database.models import Employee


def create_employee(db: Session, name: str, branch_id: int):
    """Create a new auth."""
    new_employee = Employee(name=name, branch_id=branch_id)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


def delete_employee(db: Session, employee_id: int) -> bool:
    """Delete an auth by ID."""
    employee = db.query(Employee).filter(Employee.id == employee_id).one_or_none()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False


def list_employees(db: Session):
    """List all employees."""
    return db.query(Employee).all()
