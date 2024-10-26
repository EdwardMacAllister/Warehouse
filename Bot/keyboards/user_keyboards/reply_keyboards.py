from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def accept_cancel_keyboard():
    """Create a reply keyboard with Accept and Cancel options."""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    # Define the buttons
    btn_accept = KeyboardButton("✔️ Accept")
    btn_cancel = KeyboardButton("❌ Cancel")

    # Add buttons to the keyboard
    keyboard.add(btn_accept, btn_cancel)

    return keyboard
