from aiogram import Router, types
from aiogram.filters import Command  # Import Command filter
from Bot.utils.user_utils import verify_user_credentials
from Bot.users import login, logout

auth_router = Router()


@auth_router.message(Command("login"))  # Correctly register command using the Command filter
async def cmd_login(message: types.Message):
    args = message.get_args().split()
    if len(args) < 2:
        await message.reply("Пожалуйста, введите имя пользователя и пароль.")
        return

    username = args[0]
    password = args[1]

    user_id = await verify_user_credentials(username, password)  # Use async
    if user_id:
        await login(user_id)
        await message.reply("Вы успешно вошли в систему.")
    else:
        await message.reply("Неверные учетные данные.")


@auth_router.message(Command("logout"))  # Correctly register command using the Command filter
async def cmd_logout(message: types.Message):
    user_id = message.from_user.id
    if await logout(user_id):  # Ensure logout is an async function
        await message.reply("Вы успешно вышли из системы.")
    else:
        await message.reply("Ошибка выхода. Пользователь не найден.")
