from typing import Any

from passlib.handlers.bcrypt import bcrypt
from sqlalchemy.orm import Session
from Bot.database.models import User  # Ensure User model is imported


def is_superadmin(user_id: int, db: Session) -> bool:
    """Check if the user is a superadmin."""
    user = db.query(User).filter(User.id == user_id).first()
    return user.role == 'superadmin' if user else False


def authenticate_user(username: str, password: str, db: Session) -> Any | None:
    """Authenticate a user by username and password."""
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return user
    return None
