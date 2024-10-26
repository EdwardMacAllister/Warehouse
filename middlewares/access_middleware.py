from abc import ABC

from aiogram import BaseMiddleware
from aiogram import types
from aiogram import Dispatcher
from Bot.utils.user_utils import user_exists, get_user_role


async def on_pre_process_message(message: types.Message, data: dict):
    user_id = message.from_user.id

    # Check if user exists
    if not user_exists(user_id):
        await message.reply("Вы не зарегистрированы в системе. Пожалуйста, зарегистрируйтесь.")
        return

    # Get user role
    role = get_user_role(user_id)
    if role is None:
        await message.reply("Не удалось получить вашу роль. Обратитесь к администратору.")
        return

    # Attach user role to the message data for use in handlers
    data['user_role'] = role


class AccessMiddleware(BaseMiddleware, ABC):
    def __init__(self):
        super().__init__()


# Function to register the middleware
def setup_middleware(dp: Dispatcher):
    dp.middleware.setup(AccessMiddleware())
