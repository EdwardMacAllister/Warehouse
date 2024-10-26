from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def employee_inline_keyboard():
    """Creates an inline keyboard for auth actions."""
    buttons = [
        InlineKeyboardButton(text="📋 Просмотреть инвентарь", callback_data="view_inventory"),
        InlineKeyboardButton(text="📊 Генерировать ежедневный отчет", callback_data="generate_daily_report"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
