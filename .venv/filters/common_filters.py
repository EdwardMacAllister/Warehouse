from sqlalchemy import and_


def common_filter(query, start_date=None, end_date=None, id_column=None, id_value=None, min_amount=None,
                  max_amount=None):
    """
    Универсальный фильтр для сущностей с параметрами фильтрации по дате, ID и сумме.

    :param query: Исходный SQLAlchemy query объект
    :param start_date: Начальная дата для фильтрации
    :param end_date: Конечная дата для фильтрации
    :param id_column: Столбец, по которому производится фильтрация (например, branch_id, customer_id)
    :param id_value: Значение для фильтрации по ID (например, конкретный branch_id или customer_id)
    :param min_amount: Минимальная сумма
    :param max_amount: Максимальная сумма
    :return: Отфильтрованный запрос
    """

    filters = []

    # Фильтрация по дате
    if start_date:
        filters.append(query.entity.expense_date >= start_date)
    if end_date:
        filters.append(query.entity.expense_date <= end_date)

    # Фильтрация по ID (например, филиал или клиент)
    if id_column and id_value:
        filters.append(id_column == id_value)

    # Фильтрация по сумме
    if min_amount is not None:
        filters.append(query.entity.amount >= min_amount)
    if max_amount is not None:
        filters.append(query.entity.amount <= max_amount)

    # Применение всех фильтров
    return query.filter(and_(*filters))
