from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def orders_inline_keyboard():
    """Creates an inline keyboard for orders management."""
    buttons = [
        InlineKeyboardButton(text="➕ Добавить заказ", callback_data="add_order"),
        InlineKeyboardButton(text="🗑️ Удалить заказ", callback_data="delete_order"),
        InlineKeyboardButton(text="📊 Просмотреть заказы", callback_data="view_orders"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
