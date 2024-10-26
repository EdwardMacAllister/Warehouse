from Bot.database.session import SessionLocal
from Bot.database.models import Sale


def filter_sales(start_date=None, end_date=None, branch_id=None, product_id=None):
    """
    Фильтрация продаж по дате, филиалу и продукту.

    :param start_date: Начальная дата для фильтрации
    :param end_date: Конечная дата для фильтрации
    :param branch_id: ID филиала
    :param product_id: ID продукта
    :return: Отфильтрованные продажи
    """
    session = SessionLocal()
    try:
        query = session.query(Sale)

        # Фильтрация по дате
        if start_date:
            query = query.filter(Sale.sale_date >= start_date)
        if end_date:
            query = query.filter(Sale.sale_date <= end_date)

        # Фильтрация по филиалу
        if branch_id:
            query = query.filter(Sale.branch_id == branch_id)

        # Фильтрация по продукту
        if product_id:
            query = query.filter(Sale.product_id == product_id)

        return query.all()
    finally:
        session.close()
