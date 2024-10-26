from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def report_inline_keyboard():
    """Creates an inline keyboard for report generation."""
    buttons = [
        InlineKeyboardButton(text="📊 Генерировать ежедневный отчет", callback_data="generate_daily_report"),
        InlineKeyboardButton(text="📈 Генерировать отчет по продажам", callback_data="generate_sales_report"),
    ]
    return InlineKeyboardMarkup(row_width=1).add(*buttons)
