from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def superadmin_inline_keyboard():
    """Creates an inline keyboard for superadmin actions."""
    buttons = [
        InlineKeyboardButton(text="➕ Создать филиал", callback_data="create_branch"),
        InlineKeyboardButton(text="🗑️ Удалить филиал", callback_data="delete_branch"),
        InlineKeyboardButton(text="📝 Управление пользователями", callback_data="manage_users"),
        InlineKeyboardButton(text="📈 Генерация отчетов", callback_data="generate_reports"),
        InlineKeyboardButton(text="📦 Управление товарами", callback_data="manage_inventory"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
