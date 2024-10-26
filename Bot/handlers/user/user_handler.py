import logging
import bcrypt  # Import bcrypt for password hashing
from aiogram import Router, types, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.database.session import SessionLocal
from Bot.database.crud.users.user_crud import create_user

# Initialize router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define states for user registration
class UserRegistrationStates(StatesGroup):
    awaiting_user_info = State()


@router.message(Command("register"))
async def cmd_register(message: types.Message, state: FSMContext):
    """Handler for user registration command."""
    await message.answer("Please provide username and password in the format: username password.")
    await state.set_state(UserRegistrationStates.awaiting_user_info)  # Set the state for waiting for user info


@router.message(UserRegistrationStates.awaiting_user_info)
async def process_register_info(message: types.Message, state: FSMContext):
    """Process the user info for registration."""
    try:
        # Expecting input in the format "username password"
        username, password = message.text.split(maxsplit=1)

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        with SessionLocal() as db:
            # Create user in the database
            create_user(db, username, password_hash, 'user')  # Set role as needed
            await message.answer("User registered successfully.")
            logging.info(f"User '{username}' registered successfully.")

    except ValueError:
        await message.answer("Please provide both username and password.")
        logging.warning("Registration failed due to missing username or password.")
    except Exception as e:
        await message.answer("An error occurred during registration.")
        logging.error(f"Error during user registration: {e}")

    await state.finish()  # Finish the state after processing


def register_user_handlers(dp: Dispatcher):
    """Register user handlers."""
    dp.include_router(router)  # Include the router with the handlers defined
