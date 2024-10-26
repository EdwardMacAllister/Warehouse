from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_menu_keyboard():
    """Create an inline keyboard for user actions."""
    # Create buttons
    register_button = InlineKeyboardButton(text="🔑 Регистрация", callback_data="register_user")
    login_button = InlineKeyboardButton(text="🔐 Войти", callback_data="login_user")

    # Create the inline keyboard layout
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[register_button, login_button]])  # Create the layout
    return keyboard
