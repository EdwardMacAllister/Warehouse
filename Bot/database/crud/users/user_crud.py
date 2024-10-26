from sqlalchemy.orm import Session
from sqlalchemy import select
from Bot.database.models.user import User


def create_user(db: Session, username: str, password_hash: str, role: str):
    new_user = User(username=username, password_hash=password_hash, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user(db: Session, username: str):
    user = db.execute(select(User).where(User.username == username)).scalar_one_or_none()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def list_users(db: Session):
    return db.execute(select(User)).scalars().all()
