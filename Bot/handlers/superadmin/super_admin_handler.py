import logging
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Bot.database.crud.branches.branch_crud import create_branch, list_branches, update_branch, delete_branch
from Bot.database.session import SessionLocal
from Bot.keyboards.callback_keyboards import superadmin_callback_keyboard
from Bot.utils import user_exists, get_user_role

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define states for handling branches
class BranchStates(StatesGroup):
    awaiting_branch_info = State()  # State for creating a branch
    awaiting_update_info = State()  # State for updating a branch
    awaiting_delete_info = State()  # State for deleting a branch


async def cmd_show_superadmin_menu(message: types.Message):
    """Show a superadmin menu with options."""
    await message.answer("Выберите действие:", reply_markup=superadmin_callback_keyboard())


@router.message(Command('create_branch'))
async def cmd_create_branch(message: types.Message):
    """Handler for creating a new branch."""
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Super Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    await message.answer("Введите имя филиала и местоположение в формате: имя местоположение.")
    await BranchStates.awaiting_branch_info.set()  # Set state for branch info input


@router.message(BranchStates.awaiting_branch_info)
async def process_create_branch_info(message: types.Message, state: FSMContext):
    """Process branch creation input."""
    user_id = message.from_user.id
    try:
        branch_name, location = message.text.split(maxsplit=1)  # Split input into name and location

        with SessionLocal() as db:  # Use context manager for the database session
            branch = create_branch(db, branch_name, location)  # Create branch
            await message.reply(f"Филиал '{branch_name}' создан с ID: {branch.id}")
            logging.info(f"Branch '{branch_name}' created by user ID {user_id}.")
    except ValueError:
        await message.reply("Неверный формат. Пожалуйста, введите имя и местоположение через пробел.")
    except Exception as e:
        await message.reply("Ошибка при создании филиала.")
        logging.error(f"Error creating branch: {e}")

    await state.finish()  # Reset the state


@router.message(Command('get_branch'))
async def cmd_get_branch(message: types.Message):
    """Handler for retrieving branch information."""
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Super Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    try:
        branch_id = int(message.get_args())  # Get the branch ID from the command arguments
        with SessionLocal() as db:  # Use context manager for the database session
            branch = list_branches(db, branch_id)  # Get branch info by ID

            if branch:
                await message.reply(f"Филиал ID: {branch.id}, Имя: {branch.name}, Локация: {branch.location}")
            else:
                await message.reply(f"Филиал с ID {branch_id} не найден.")
    except ValueError:
        await message.reply("Пожалуйста, введите корректный ID филиала.")
    except Exception as e:
        await message.reply("Ошибка при получении информации о филиале.")
        logging.error(f"Error retrieving branch: {e}")


@router.message(Command('update_branch'))
async def cmd_update_branch(message: types.Message):
    """Handler for updating branch information."""
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Super Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    await message.answer("Введите ID филиала, новое имя и новое местоположение в формате: ID имя местоположение.")
    await BranchStates.awaiting_update_info.set()  # Set the state for update input


@router.message(BranchStates.awaiting_update_info)
async def process_update_branch_info(message: types.Message, state: FSMContext):
    """Process the input for updating a branch."""
    user_id = message.from_user.id
    try:
        branch_id, new_name, new_location = message.text.split(maxsplit=2)  # Split input into ID, name, and location

        with SessionLocal() as db:  # Use context manager for the database session
            updated_branch = update_branch(db, int(branch_id), new_name, new_location)  # Update branch info

            if updated_branch:
                await message.reply(f"Филиал ID {branch_id} успешно обновлён.")
                logging.info(f"Branch ID {branch_id} updated by user ID {user_id}.")
            else:
                await message.reply(f"Филиал с ID {branch_id} не найден.")
    except ValueError:
        await message.reply("Пожалуйста, введите корректные данные.")
    except Exception as e:
        await message.reply("Ошибка при обновлении филиала.")
        logging.error(f"Error updating branch: {e}")

    await state.finish()  # Reset the state


@router.message(Command('delete_branch'))
async def cmd_delete_branch(message: types.Message):
    """Handler for deleting a branch."""
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Super Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    await message.answer("Введите ID филиала, который хотите удалить.")
    await BranchStates.awaiting_delete_info.set()  # Set the state for delete input


@router.message(BranchStates.awaiting_delete_info)
async def process_delete_branch_info(message: types.Message, state: FSMContext):
    """Process the input for deleting a branch."""
    user_id = message.from_user.id
    try:
        branch_id = int(message.text)  # Get the branch ID from the message

        with SessionLocal() as db:  # Use context manager for the database session
            success = delete_branch(db, branch_id)  # Delete branch by ID

            if success:
                await message.reply(f"Филиал ID {branch_id} успешно удалён.")
                logging.info(f"Branch ID {branch_id} deleted by user ID {user_id}.")
            else:
                await message.reply(f"Филиал с ID {branch_id} не найден.")
    except ValueError:
        await message.reply("Пожалуйста, введите корректный ID филиала.")
    except Exception as e:
        await message.reply("Ошибка при удалении филиала.")
        logging.error(f"Error deleting branch: {e}")

    await state.finish()  # Reset the state


def register_super_admin_handlers(dp: Dispatcher):
    """Register all superadmin handlers."""
    dp.register_message_handler(cmd_show_superadmin_menu, Command("superadmin_menu"))
    dp.register_message_handler(cmd_create_branch, Command("create_branch"))
    dp.register_message_handler(cmd_get_branch, Command("get_branch"))
    dp.register_message_handler(cmd_update_branch, Command("update_branch"))
    dp.register_message_handler(cmd_delete_branch, Command("delete_branch"))
