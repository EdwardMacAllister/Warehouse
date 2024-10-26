from Bot.database.models import User
from Bot.database.session import SessionLocal


def get_user_role(user_id):
    """
    Возвращает роль пользователя на основе его ID.

    :param user_id: ID пользователя
    :return: Роль пользователя (например, "Employee", "Admin", "Super Admin")
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            return user.role
        return None
    finally:
        session.close()
