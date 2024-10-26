from Bot.database.models import User
from Bot.database.session import SessionLocal


def check_login(username, password):
    """
    Проверка правильности логина пользователя.

    :param username: Имя пользователя
    :param password: Пароль пользователя
    :return: True, если логин и пароль верны, иначе False
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user and user.password == password:
            return True
        return False
    finally:
        session.close()
