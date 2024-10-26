from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def admin_main_screen_keyboard():
    """Creates the main screen keyboard for admin actions."""
    buttons = [
        [KeyboardButton("👤 Управление пользователями")],
        [KeyboardButton("📊 Генерировать отчеты")],
        [KeyboardButton("📦 Управление товарами")],
        [KeyboardButton("🌳 Управление филиалами")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def employee_main_screen_keyboard():
    """Creates the main screen keyboard for auth actions."""
    buttons = [
        [KeyboardButton("📋 Просмотреть инвентарь")],
        [KeyboardButton("📊 Генерировать ежедневный отчет")],
        [KeyboardButton("💸 Просмотреть расходы")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def superadmin_main_screen_keyboard():
    """Creates the main screen keyboard for superadmin actions."""
    buttons = [
        [KeyboardButton("➕ Создать филиал")],
        [KeyboardButton("📝 Управление пользователями")],
        [KeyboardButton("📈 Генерация отчетов")],
        [KeyboardButton("📦 Управление товарами")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
