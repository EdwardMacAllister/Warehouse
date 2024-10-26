from Bot.database.models import User
from Bot.database.session import SessionLocal


def user_exists(user_id):
    """
    Проверяет, существует ли пользователь в базе данных.

    :param user_id: ID пользователя
    :return: True, если пользователь существует, иначе False
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user is not None
    finally:
        session.close()
