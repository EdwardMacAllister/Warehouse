# Bot/handlers/employee_handler.py

import logging
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.database.session import SessionLocal
from Bot.database.crud.employees.employee_crud import create_employee, list_employees, delete_employee
from Bot.keyboards.employee_keyboards.employee_main_keyboards import employee_inline_keyboard

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define states for employee management
class EmployeeStates(StatesGroup):
    waiting_for_employee_info = State()  # State for waiting for employee info
    waiting_for_delete_info = State()  # State for waiting for employee ID to delete


@router.message(Command('employee_menu'))
async def cmd_show_employee_menu(message: types.Message):
    """Show the employee management menu."""
    await message.answer("Управление сотрудниками:", reply_markup=employee_inline_keyboard())


@router.message(Command('add_employee'))
async def cmd_add_employee(message: types.Message):
    """Start the process of adding a new employee."""
    await message.answer("Введите имя и должность сотрудника в формате: имя должность.")
    await EmployeeStates.waiting_for_employee_info.set()  # Set the state


@router.message(EmployeeStates.waiting_for_employee_info)
async def process_add_employee_info(message: types.Message, state: FSMContext):
    """Process the employee's name and position."""
    try:
        name, position = message.text.split()
        with SessionLocal() as db:
            employee = create_employee(db, name=name, position=position)
            await message.answer(f"Сотрудник '{employee.name}' добавлен с ID: {employee.id}.")
    except ValueError:
        await message.answer("Пожалуйста, введите имя и должность в правильном формате.")
    except Exception as e:
        logging.error(f"Error adding employee: {e}")
        await message.answer("Ошибка при добавлении сотрудника.")

    await state.finish()  # Reset the state


@router.message(Command('view_employees'))
async def cmd_view_employees(message: types.Message):
    """Show a list of employees."""
    with SessionLocal() as db:
        employees = list_employees(db)
        if employees:
            response = "\n".join([f"ID: {emp.id}, Имя: {emp.name}, Должность: {emp.position}" for emp in employees])
            await message.answer(response)
        else:
            await message.answer("Сотрудники не найдены.")


@router.message(Command('delete_employee'))
async def cmd_delete_employee(message: types.Message):
    """Start the process of deleting an employee."""
    await message.answer("Введите ID сотрудника, которого хотите удалить.")
    await EmployeeStates.waiting_for_delete_info.set()  # Set the state for deletion


@router.message(EmployeeStates.waiting_for_delete_info)
async def process_delete_employee_info(message: types.Message, state: FSMContext):
    """Process the deletion of an employee."""
    try:
        employee_id = int(message.text)
        with SessionLocal() as db:
            success = delete_employee(db, employee_id)
            if success:
                await message.answer(f"Сотрудник ID {employee_id} успешно удалён.")
            else:
                await message.answer("Сотрудник не найден.")
    except ValueError:
        await message.answer("Пожалуйста, введите корректный ID сотрудника.")
    except Exception as e:
        logging.error(f"Error deleting employee: {e}")
        await message.answer("Ошибка при удалении сотрудника.")

    await state.finish()  # Reset the state


def register_employee_handlers(dp: Dispatcher):
    dp.include_router(router)  # Register the router with the dispatcher
