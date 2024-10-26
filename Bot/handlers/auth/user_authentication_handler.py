import logging
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import bcrypt

from Bot.database.session import get_db
from Bot.database.models import User
from Bot.keyboards.user_keyboards.inline_keyboards import user_menu_keyboard
from Bot.keyboards.user_keyboards.reply_keyboards import accept_cancel_keyboard

# Initialize the router
router = Router()

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define states for user actions
class UserActionsStates(StatesGroup):
    waiting_for_username_password = State()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    """Handler for the /start command."""
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=user_menu_keyboard())


@router.message(Command('create_user'))
async def cmd_create_user(message: types.Message, state: FSMContext):
    """Handler for creating a new user."""
    await message.answer("Пожалуйста, введите имя пользователя и пароль в формате: username password.")
    await state.set_state(UserActionsStates.waiting_for_username_password)


@router.message(UserActionsStates.waiting_for_username_password)
async def process_create_user(message: types.Message, state: FSMContext):
    """Process the username and password input for creating a new user."""
    args = message.text.split()

    if len(args) < 2:
        await message.reply("Пожалуйста, введите имя пользователя и пароль.")
        return

    username = args[0]
    password = args[1]

    # Use the database session with the context manager
    db = get_db()
    try:
        with db() as session:  # Use session context manager
            existing_user = session.query(User).filter(User.username == username).first()
            if existing_user:
                await message.reply("Имя пользователя уже существует.")
                return

            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_user = User(username=username, password_hash=password_hash)
            session.add(new_user)
            session.commit()
            await message.reply(f"Пользователь {username} создан.", reply_markup=user_menu_keyboard())
    except Exception as e:
        logging.error(f"Error adding user: {e}")
        await message.reply("Ошибка при создании пользователя. Пожалуйста, попробуйте снова.")


@router.message(Command('login'))
async def cmd_login(message: types.Message, state: FSMContext):
    """Handler for logging in a user."""
    await message.answer("Пожалуйста, введите имя пользователя и пароль в формате: username password.")
    await state.set_state(UserActionsStates.waiting_for_username_password)


@router.message(UserActionsStates.waiting_for_username_password)
async def process_login(message: types.Message, state: FSMContext):
    """Process the username and password input for logging in a user."""
    args = message.text.split()

    if len(args) < 2:
        await message.reply("Пожалуйста, введите имя пользователя и пароль.")
        return

    username = args[0]
    password = args[1]

    db = get_db()
    try:
        with db() as session:  # Use session context manager
            user = session.query(User).filter(User.username == username).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                await message.reply("Вы успешно вошли в систему.", reply_markup=accept_cancel_keyboard())
            else:
                await message.reply("Неверные учетные данные. Пожалуйста, проверьте имя пользователя и пароль.")
    except Exception as e:
        logging.error(f"Error logging in: {e}")
        await message.reply("Ошибка при попытке войти в систему. Пожалуйста, попробуйте снова.")


def register_auth_handlers(dp: Dispatcher):
    """Register authentication handlers."""
    dp.include_router(router)  # Register the router
