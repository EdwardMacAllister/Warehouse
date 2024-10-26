from aiogram import types
from dispatcher import Dispatcher


async def handle_add_product(callback_query: types.CallbackQuery):
    """Handle add product callback for admin."""
    await callback_query.answer("Форма для добавления товара открыта.")


async def handle_delete_product(callback_query: types.CallbackQuery):
    """Handle delete product callback for admin."""
    await callback_query.answer("Форма для удаления товара открыта.")


async def handle_view_products(callback_query: types.CallbackQuery):
    """Handle view products callback for admin."""
    await callback_query.answer("Вот список ваших товаров.")


def register_admin_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(handle_add_product, text="add_product")
    dp.register_callback_query_handler(handle_delete_product, text="delete_product")
    dp.register_callback_query_handler(handle_view_products, text="view_products")
