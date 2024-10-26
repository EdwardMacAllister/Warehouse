from sqlalchemy.orm import Session
from sqlalchemy import select
from Bot.database.models.branches import Branch


def create_branch(db: Session, name: str, location: str):
    """Create a new branch."""
    new_branch = Branch(name=name, location=location)
    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)
    return new_branch


def delete_branch(db: Session, branch_id: int) -> bool:
    """Delete a branch by ID."""
    stmt = select(Branch).where(Branch.id == branch_id)
    branch = db.execute(stmt).scalar_one_or_none()
    if branch:
        db.delete(branch)
        db.commit()
        return True
    return False


def update_branch(db: Session, branch_id: int, name: str = None, location: str = None):
    """Update an existing branch."""
    stmt = select(Branch).where(Branch.id == branch_id)
    branch = db.execute(stmt).scalar_one_or_none()
    if branch:
        if name is not None:
            branch.name = name
        if location is not None:
            branch.location = location
        db.commit()
        return branch
    return None


def list_branches(db: Session):
    """List all branches."""
    stmt = select(Branch)
    return db.execute(stmt).scalars().all()
