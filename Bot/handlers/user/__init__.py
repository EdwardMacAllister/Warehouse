from aiogram import Dispatcher

from .user_handler import register_user_handlers


def register_users_handlers(dp: Dispatcher):
    register_user_handlers(dp)
