import datetime  # Убедитесь, что datetime импортирован

from Bot.database.models import User
from Bot.database.session import SessionLocal


def login(user_id):
    """
    Выполняет авторизацию пользователя, обновляя информацию о его последнем входе в систему.

    :param user_id: ID пользователя
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.last_login = datetime.datetime.now(datetime.UTC)  # Обновляем время последнего логина
            session.commit()
            return True  # Логин успешен
        return False  # Пользователь не найден
    finally:
        session.close()
