from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inventory_inline_keyboard():
    """Creates an inline keyboard for inventory management."""
    buttons = [
        InlineKeyboardButton(text="➕ Добавить товар в инвентарь", callback_data="add_inventory_item"),
        InlineKeyboardButton(text="🗑️ Удалить товар из инвентаря", callback_data="delete_inventory_item"),
        InlineKeyboardButton(text="📋 Просмотреть инвентарь", callback_data="view_inventory"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
