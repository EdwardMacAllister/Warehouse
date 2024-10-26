from sqlalchemy.orm import Session
from Bot.database.models import Expense


def create_expense(db: Session, amount: float, description: str):
    """Create a new expense."""
    new_expense = Expense(amount=amount, description=description)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def delete_expense(db: Session, expense_id: int) -> bool:
    """Delete an expense by ID."""
    expense = db.query(Expense).filter(Expense.id == expense_id).one_or_none()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False


def list_expenses(db: Session):
    """List all expenses."""
    return db.query(Expense).all()
