from aiogram import Router, types
from aiogram.filters import Command  # Import the Command filter
from Bot.users import user_exists, get_user_role
from Bot.database.crud.branches.branch_crud import create_branch

superadmin_router = Router()


@superadmin_router.message(Command("create_branch"))  # Use Command filter for creating a branch
async def cmd_create_branch(message: types.Message):
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Super Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    branch_name = "Main Branch"  # Replace with actual input from the user
    location = "Downtown"  # Replace with actual input from the user
    branch = await create_branch(branch_name, location)  # Ensure create_branch is async
    await message.reply(f"Филиал '{branch_name}' создан с ID: {branch.id}.")
