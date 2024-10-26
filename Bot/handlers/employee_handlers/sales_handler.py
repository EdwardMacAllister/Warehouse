import logging
from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.database.crud.sales.sales_crud import create_sale, list_sales, delete_sale
from Bot.database.session import SessionLocal
from Bot.keyboards.admin_keyboards.saler_keyboards import saler_inline_keyboard

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define the states for handling sales
class SaleStates(StatesGroup):
    waiting_for_sale_info = State()  # State for waiting for sale info
    waiting_for_update_info = State()  # State for waiting for update info


@router.message(Command('sales_menu'))
async def cmd_show_sales_menu(message: types.Message):
    await message.answer("Управление продажами:", reply_markup=saler_inline_keyboard())


@router.message(Command('add_sale'))
async def cmd_add_sale(message: types.Message, state: FSMContext):
    await message.answer("Введите сумму и описание продажи в формате: сумма описание.")
    await state.set_state(SaleStates.waiting_for_sale_info)  # Set the state for sale info


@router.message(SaleStates.waiting_for_sale_info)  # Directly use the state here
async def process_add_sale(message: types.Message, state: FSMContext):
    try:
        amount, description = message.text.split(maxsplit=1)
        amount = float(amount)  # Convert amount to float
    except ValueError:
        await message.answer("Неверный формат. Пожалуйста, введите сумму и описание через пробел.")
        return

    with SessionLocal() as db:
        try:
            sale = create_sale(db, amount, description)
            await message.answer(f"Продажа '{description}' на сумму {amount} добавлена с ID: {sale.id}")
        except Exception as e:
            logging.error(f"Error adding sale: {e}")
            await message.answer("Ошибка при добавлении продажи.")
    await state.finish()  # Reset the state


@router.message(Command('get_sale'))
async def cmd_get_sale(message: types.Message):
    try:
        sale_id = int(message.get_args())
    except ValueError:
        await message.answer("Пожалуйста, введите корректный ID продажи.")
        return

    with SessionLocal() as db:
        sale = list_sales(db, sale_id)
        if sale:
            await message.answer(f"Продажа ID: {sale.id}, Сумма: {sale.amount}, Описание: {sale.description}")
        else:
            await message.answer(f"Продажа с ID {sale_id} не найдена.")


@router.message(Command('delete_sale'))
async def cmd_delete_sale(message: types.Message):
    try:
        sale_id = int(message.get_args())
    except ValueError:
        await message.answer("Пожалуйста, введите корректный ID продажи.")
        return

    with SessionLocal() as db:
        try:
            if delete_sale(db, sale_id):
                await message.answer(f"Продажа ID {sale_id} успешно удалена.")
            else:
                await message.answer(f"Продажа с ID {sale_id} не найдена.")
        except Exception as e:
            logging.error(f"Error deleting sale: {e}")
            await message.answer("Ошибка при удалении продажи.")


@router.message(Command('list_sales'))
async def cmd_list_sales(message: types.Message):
    with SessionLocal() as db:
        sales = list_sales(db)
        if sales:
            response = "\n".join(
                [f"ID: {sale.id}, Сумма: {sale.amount}, Описание: {sale.description}" for sale in sales])
            await message.answer(response)
        else:
            await message.answer("Нет продаж в базе данных.")


def register_sales_handlers(dp: Dispatcher):
    dp.include_router(router)  # Register the router
