from Bot.database.session import SessionLocal
from Bot.database.models import Order
from Bot.filters.common_filters import common_filter


def filter_orders(start_date=None, end_date=None, customer_id=None, min_total_price=None, max_total_price=None):
    """
    Фильтрация заказов по дате, клиенту и сумме заказа.
    """
    session = SessionLocal()
    try:
        query = session.query(Order)

        # Используем общий фильтр
        query = common_filter(query, start_date=start_date, end_date=end_date, id_column=Order.customer_id,
                              id_value=customer_id, min_amount=min_total_price, max_amount=max_total_price)

        return query.all()
    finally:
        session.close()
