from aiogram import types


def employee_inline_keyboard() -> types.InlineKeyboardMarkup:
    """Creates an inline keyboard for auth management."""
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    # Define buttons
    add_employee_button = types.InlineKeyboardButton("Добавить сотрудника", callback_data="add_employee")
    view_employees_button = types.InlineKeyboardButton("Просмотреть сотрудников", callback_data="view_employees")
    update_employee_button = types.InlineKeyboardButton("Обновить сотрудника", callback_data="update_employee")
    delete_employee_button = types.InlineKeyboardButton("Удалить сотрудника", callback_data="delete_employee")

    # Add buttons to the keyboard
    keyboard.add(add_employee_button, view_employees_button)
    keyboard.add(update_employee_button, delete_employee_button)

    return keyboard


def sales_inline_keyboard() -> types.InlineKeyboardMarkup:
    """Creates an inline keyboard for sales management."""
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    # Define buttons
    add_sale_button = types.InlineKeyboardButton("Добавить продажу", callback_data="add_sale")
    view_sales_button = types.InlineKeyboardButton("Просмотреть продажи", callback_data="view_sales")
    update_sale_button = types.InlineKeyboardButton("Обновить продажу", callback_data="update_sale")
    delete_sale_button = types.InlineKeyboardButton("Удалить продажу", callback_data="delete_sale")

    # Add buttons to the keyboard
    keyboard.add(add_sale_button, view_sales_button)
    keyboard.add(update_sale_button, delete_sale_button)

    return keyboard
