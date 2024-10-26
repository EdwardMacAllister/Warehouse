from Bot.database.session import SessionLocal
from Bot.database.models import Expense
from Bot.filters.common_filters import common_filter


def filter_expenses(start_date=None, end_date=None, branch_id=None, min_amount=None, max_amount=None):
    """
    Фильтрация расходов по дате, филиалу и сумме.
    """
    session = SessionLocal()
    try:
        query = session.query(Expense)

        # Используем общий фильтр
        query = common_filter(query, start_date=start_date, end_date=end_date, id_column=Expense.branch_id,
                              id_value=branch_id, min_amount=min_amount, max_amount=max_amount)

        return query.all()
    finally:
        session.close()
