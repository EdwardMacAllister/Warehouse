from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def saler_inline_keyboard():
    """Creates an inline keyboard for sales management."""
    buttons = [
        InlineKeyboardButton(text="➕ Добавить продажу", callback_data="add_sale"),
        InlineKeyboardButton(text="🗑️ Удалить продажу", callback_data="delete_sale"),
        InlineKeyboardButton(text="📊 Просмотреть продажи", callback_data="view_sales"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
