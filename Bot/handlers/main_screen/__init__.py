from aiogram import Dispatcher

from .main_screen_handler import register_main_screen_handlers


def register_screen_handlers(dp: Dispatcher):
    register_main_screen_handlers(dp)
