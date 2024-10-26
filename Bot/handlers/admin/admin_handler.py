import logging
import bcrypt  # Ensure bcrypt is imported for password hashing
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from Bot.database.models.user import User
from Bot.database.crud.users.user_crud import create_user, delete_user
from Bot.database.session import SessionLocal  # Ensure to import your session

# Initialize router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define the states for the admin handlers
class AdminStates(StatesGroup):
    add_user = State()  # State for adding a user
    password = State()  # State for entering the password
    remove_user = State()  # State for removing a user


def is_superadmin(user_id: int, db) -> bool:
    """Check if the user is a superadmin."""
    user = db.query(User).filter(User.id == user_id).first()
    return user.role == 'superadmin' if user else False


@router.message(Command('add_user'))
async def cmd_add_user(message: types.Message):
    """Handler for adding a new user."""
    user_id = message.from_user.id

    with SessionLocal() as db:  # Use context manager for session
        if not is_superadmin(user_id, db):
            await message.answer("У вас нет доступа к этой команде.")
            return

    await AdminStates.add_user.set()  # Set the state for username input
    await message.answer("Введите имя пользователя нового пользователя:")


@router.message(AdminStates.add_user)  # Updated to use the state filter correctly
async def process_add_user_username(message: types.Message, state: FSMContext):
    """Process the username input for adding a new user."""
    username = message.text
    await state.update_data(username=username)  # Store the username

    await AdminStates.password.set()  # Move to the next state for password
    await message.answer("Введите пароль для нового пользователя:")


@router.message(AdminStates.password)  # Updated to use the state filter correctly
async def process_add_user_password(message: types.Message, state: FSMContext):
    """Process the password input for adding a new user."""
    password = message.text
    data = await state.get_data()
    username = data.get("username")

    with SessionLocal() as db:  # Use context manager for session
        try:
            # Hash the password before saving it
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            create_user(db=db, username=username, password=password_hash, role='user')  # Set role as needed
            await message.answer("Пользователь успешно добавлен!")
            logging.info(f"User {username} created successfully by admin {message.from_user.username}.")
        except Exception as e:
            await message.answer("Ошибка при добавлении пользователя.")
            logging.error(f"Error adding user: {e}")

    await state.finish()  # Reset the state


@router.message(Command('remove_user'))
async def cmd_remove_user(message: types.Message):
    """Handler for removing a user."""
    user_id = message.from_user.id

    with SessionLocal() as db:  # Use context manager for session
        if not is_superadmin(user_id, db):
            await message.answer("У вас нет доступа к этой команде.")
            return

    await AdminStates.remove_user.set()  # Set the state for username input
    await message.answer("Введите имя пользователя, которого хотите удалить:")


@router.message(AdminStates.remove_user)  # Updated to use the state filter correctly
async def process_remove_user(message: types.Message, state: FSMContext):
    """Process the input for removing a user."""
    username = message.text

    with SessionLocal() as db:  # Use context manager for session
        try:
            if delete_user(db=db, username=username):  # Call delete_user function
                await message.answer(f"Пользователь {username} успешно удален!")
                logging.info(f"User {username} removed successfully by admin {message.from_user.username}.")
            else:
                await message.answer("Пользователь не найден.")
                logging.warning(f"Attempted to remove non-existent user: {username}.")
        except Exception as e:
            await message.answer("Ошибка при удалении пользователя.")
            logging.error(f"Error removing user: {e}")

    await state.finish()  # Reset the state


def register_admin_handlers(dp: Dispatcher):
    """Register all admin handlers."""
    dp.include_router(router)  # Include the router with all admin handlers
