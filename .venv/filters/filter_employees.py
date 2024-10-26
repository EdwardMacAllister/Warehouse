from Bot.database.session import SessionLocal
from Bot.database.models import Employee


def filter_employees(branch_id=None, position=None):
    """
    Фильтрация сотрудников по филиалу и должности.

    :param branch_id: ID филиала
    :param position: Должность сотрудника
    :return: Отфильтрованные сотрудники
    """
    session = SessionLocal()
    try:
        query = session.query(Employee)

        # Фильтрация по филиалу
        if branch_id:
            query = query.filter(Employee.branch_id == branch_id)

        # Фильтрация по должности
        if position:
            query = query.filter(Employee.position.ilike(f"%{position}%"))

        return query.all()
    finally:
        session.close()
