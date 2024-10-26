import logging

from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.database.crud.orders.orders_crud import create_order, list_orders, delete_order
from Bot.database.session import SessionLocal

# Initialize the router
router = Router()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define order states
class OrderStates(StatesGroup):
    waiting_order_id = State()  # State for waiting for order ID
    waiting_order_info = State()  # State for waiting for order info


@router.message(Command('create_order'))
async def cmd_create_order(message: types.Message, state: FSMContext):
    """Handler for creating an order."""
    await message.answer("Please provide the order details in the format: order_name order_amount.")
    await state.set_state(OrderStates.waiting_order_info)  # Set to the appropriate state


@router.message(OrderStates.waiting_order_info)  # Use the State directly
async def process_order_info(message: types.Message, state: FSMContext):
    """Process order information."""
    order_info = message.text.split()

    if len(order_info) < 2:
        await message.answer("Invalid format. Please provide the order name and amount.")
        return

    order_name = order_info[0]
    order_amount = order_info[1]

    try:
        with SessionLocal() as db:  # Use context manager for the database session
            create_order(db=db, name=order_name, amount=order_amount)  # Example of using db
            await message.answer("Order created successfully.")
    except Exception as e:
        logging.error(f"Error creating order: {e}")
        await message.answer("Error while creating the order.")

    await state.finish()  # Reset the state


@router.message(Command('view_orders'))
async def cmd_view_orders(message: types.Message):
    """Show a list of orders."""
    with SessionLocal() as db:
        orders = list_orders(db)  # Assuming this function fetches all orders and requires db session

        if orders:
            response = "\n".join(
                [f"ID: {order.id}, Товар: {order.product_name}, Количество: {order.quantity}" for order in orders])
            await message.answer(response)
        else:
            await message.answer("Заказы не найдены.")


@router.message(Command('delete_order'))
async def cmd_delete_order(message: types.Message, state: FSMContext):
    """Handler for deleting an order."""
    await message.answer("Please provide the order ID you want to delete.")
    await state.set_state(OrderStates.waiting_order_id)  # Set to the appropriate state


@router.message(OrderStates.waiting_order_id)  # Use the State directly
async def process_delete_order(message: types.Message, state: FSMContext):
    """Process the order ID for deletion."""
    order_id = message.text.strip()  # Get the order ID from the message

    if not order_id.isdigit():  # Ensure that the order ID is a digit
        await message.answer("Invalid format. Please provide a valid order ID.")
        return

    order_id = int(order_id)  # Convert to an integer

    with SessionLocal() as db:  # Use context manager for the database session
        success = delete_order(db=db, order_id=order_id)  # Call the delete function

        if success:
            await message.answer(f"Order ID {order_id} has been successfully deleted.")
        else:
            await message.answer(f"Order with ID {order_id} not found.")

    await state.finish()  # Reset the state


def register_order_handlers(dp: Dispatcher):
    """Register all order handlers."""
    dp.include_router(router)  # Register the router
