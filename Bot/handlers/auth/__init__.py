from aiogram import Dispatcher

from .user_authentication_handler import register_auth_handlers


def register_employee_handlers(dp: Dispatcher):
    register_auth_handlers(dp)
