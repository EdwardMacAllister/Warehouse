from aiogram import Dispatcher

from Bot.handlers.employee_handlers import register_admin_commands
from .admin_handler import register_admin_handlers


def register_handlers(dp: Dispatcher):
    register_admin_commands(dp)
    register_admin_handlers(dp)
