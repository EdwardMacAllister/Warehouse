from Bot.database.session import SessionLocal
from Bot.database.models import DailyReport


def filter_daily_reports(start_date=None, end_date=None, branch_id=None):
    """
    Фильтрация ежедневных отчётов по дате и филиалу.

    :param start_date: Начальная дата для фильтрации
    :param end_date: Конечная дата для фильтрации
    :param branch_id: ID филиала
    :return: Отфильтрованные отчёты
    """
    session = SessionLocal()
    try:
        query = session.query(DailyReport)

        # Фильтрация по дате
        if start_date:
            query = query.filter(DailyReport.report_date >= start_date)
        if end_date:
            query = query.filter(DailyReport.report_date <= end_date)

        # Фильтрация по филиалу
        if branch_id:
            query = query.filter(DailyReport.branch_id == branch_id)

        return query.all()
    finally:
        session.close()
