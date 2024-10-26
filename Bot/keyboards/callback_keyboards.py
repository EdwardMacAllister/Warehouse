from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Admin Callback Keyboard
def admin_callback_keyboard():
    """Creates a callback keyboard for admin actions."""
    buttons = [
        InlineKeyboardButton(text="➕ Добавить пользователя", callback_data="add_user"),
        InlineKeyboardButton(text="🗑️ Удалить пользователя", callback_data="delete_user"),
        InlineKeyboardButton(text="📊 Просмотреть отчеты", callback_data="view_reports"),
        InlineKeyboardButton(text="📦 Управление товарами", callback_data="manage_products"),
        InlineKeyboardButton(text="🌳 Управление филиалами", callback_data="manage_branches"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)


# Employee Callback Keyboard
def employee_callback_keyboard():
    """Creates a callback keyboard for auth actions."""
    buttons = [
        InlineKeyboardButton(text="📋 Просмотреть инвентарь", callback_data="view_inventory"),
        InlineKeyboardButton(text="📊 Генерировать ежедневный отчет", callback_data="generate_daily_report"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)


# Superadmin Callback Keyboard
def superadmin_callback_keyboard():
    """Creates a callback keyboard for superadmin actions."""
    buttons = [
        InlineKeyboardButton(text="➕ Создать филиал", callback_data="create_branch"),
        InlineKeyboardButton(text="🗑️ Удалить филиал", callback_data="delete_branch"),
        InlineKeyboardButton(text="📝 Управление пользователями", callback_data="manage_users"),
        InlineKeyboardButton(text="📈 Генерация отчетов", callback_data="generate_reports"),
        InlineKeyboardButton(text="📦 Управление товарами", callback_data="manage_products"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
