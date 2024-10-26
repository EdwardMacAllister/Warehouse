from aiogram import Router, types
from aiogram.filters import Command  # Import Command filter

from Bot.database.crud.employees.employee_crud import create_employee
from Bot.users import user_exists, get_user_role

admin_router = Router()


@admin_router.message(Command("create_employee"))  # Use Command filter for creating an auth
async def cmd_create_employee(message: types.Message):
    user_id = message.from_user.id

    if not user_exists(user_id) or get_user_role(user_id) != "Admin":
        await message.reply("У вас нет доступа к этой команде.")
        return

    args = message.get_args().split()
    if len(args) < 2:
        await message.reply("Пожалуйста, введите имя и должность сотрудника.")
        return

    name = args[0]
    position = args[1]
    branch_id = 1  # Example branch ID
    employee = await create_employee(name, position, branch_id)  # Ensure this is async
    await message.reply(f"Сотрудник {employee.name} создан с ID: {employee.id}.")
