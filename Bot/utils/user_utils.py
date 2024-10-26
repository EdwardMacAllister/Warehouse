from Bot.database.models import User
from Bot.database.session import SessionLocal


def user_exists(user_id):
    """Check if a user exists in the database."""
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user is not None
    finally:
        session.close()


def verify_user_credentials(username, password):
    """Verify user credentials against the database."""
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user and user.password == password:  # Ensure to hash and compare passwords securely
            return user.id
        return None
    finally:
        session.close()


def get_user_role(user_id):
    """Get the role of a user."""
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user.role if user else None
    finally:
        session.close()
