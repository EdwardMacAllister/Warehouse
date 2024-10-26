from Bot.database.session import SessionLocal
from Bot.database.models import Supplier


def filter_suppliers(name=None):
    """
    Фильтрация поставщиков по имени.

    :param name: Имя или часть имени поставщика
    :return: Отфильтрованные поставщики
    """
    session = SessionLocal()
    try:
        query = session.query(Supplier)

        # Фильтрация по имени
        if name:
            query = query.filter(Supplier.name.ilike(f"%{name}%"))

        return query.all()
    finally:
        session.close()
