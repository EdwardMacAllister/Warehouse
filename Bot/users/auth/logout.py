from Bot.database.models import User
from Bot.database.session import SessionLocal


def logout(user_id):
    """
    Выполняет выход пользователя из системы, сбрасывая его сессию или удаляя данные сессии.

    :param user_id: ID пользователя
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            # Логика для выхода может включать сброс токена, обновление статуса или удаления сессии.
            # Пример: если у вас есть поле is_logged_in в модели User
            user.is_logged_in = False  # Пример, если есть поле для отслеживания статуса
            session.commit()
            return True  # Успешный логаут
        return False  # Пользователь не найден
    finally:
        session.close()
