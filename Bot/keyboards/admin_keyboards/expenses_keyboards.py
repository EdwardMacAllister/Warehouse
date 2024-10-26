from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def expenses_inline_keyboard():
    """Creates an inline keyboard for expenses management."""
    buttons = [
        InlineKeyboardButton(text="➕ Добавить расход", callback_data="add_expense"),
        InlineKeyboardButton(text="🗑️ Удалить расход", callback_data="delete_expense"),
        InlineKeyboardButton(text="📊 Просмотреть расходы", callback_data="view_expenses"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
