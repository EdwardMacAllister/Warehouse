import logging

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Import your CRUD functions and keyboards accordingly
from Bot.database.crud.users.user_crud import create_user
from Bot.database.session import SessionLocal

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define states for SuperAdmin actions
class SuperAdminStates(StatesGroup):
    waiting_for_username = State()  # State for waiting for username input
    waiting_for_password = State()  # State for waiting for password input


@router.message(Command('create_superadmin'))
async def cmd_create_superadmin(message: types.Message, state: FSMContext):
    """Start the process of creating a new superadmin."""
    await message.answer("Please provide a username for the new superadmin:")
    await state.set_state(SuperAdminStates.waiting_for_username)  # Set state to waiting for username


@router.message(SuperAdminStates.waiting_for_username)
async def process_username(message: types.Message, state: FSMContext):
    """Process the username input."""
    username = message.text
    await state.update_data(username=username)  # Store the username

    await message.answer("Please provide a password for the new superadmin:")
    await state.set_state(SuperAdminStates.waiting_for_password)  # Set state to waiting for password


@router.message(SuperAdminStates.waiting_for_password)
async def process_password(message: types.Message, state: FSMContext):
    """Process the password input."""
    password = message.text
    data = await state.get_data()  # Get the stored username
    username = data.get('username')

    with SessionLocal() as db:  # Use context manager for the database session
        try:
            # Create the superadmin with the provided username and password
            create_user(db=db, username=username, password=password, role='superadmin')
            await message.answer(f"Superadmin '{username}' created successfully!")
            logging.info(f"Superadmin '{username}' created successfully.")
        except Exception as e:
            await message.answer("Error while creating the superadmin.")
            logging.error(f"Error creating superadmin: {e}")

    await state.finish()  # Reset the state after completion
