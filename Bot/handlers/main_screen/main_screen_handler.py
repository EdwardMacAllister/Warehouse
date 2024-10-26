# handlers/main_screen_handler.py

import logging
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command

from Bot.keyboards.main_screen_keyboards import (
    admin_main_screen_keyboard,
    employee_main_screen_keyboard,
    superadmin_main_screen_keyboard
)

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@router.message(Command('main_menu'))
async def cmd_show_main_screen(message: types.Message, user_role: str):
    """Show the main screen based on a user role."""
    if user_role == "admin":
        await message.answer("Выберите действие:", reply_markup=admin_main_screen_keyboard())
    elif user_role == "auth":
        await message.answer("Выберите действие:", reply_markup=employee_main_screen_keyboard())
    elif user_role == "superadmin":
        await message.answer("Выберите действие:", reply_markup=superadmin_main_screen_keyboard())
    else:
        await message.answer("Неизвестная роль.")


def register_main_screen_handlers(dp: Dispatcher):
    """Register main screen handlers."""
    dp.include_router(router)  # Include the router with the handlers defined
