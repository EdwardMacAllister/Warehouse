from aiogram import types
from dispatcher import Dispatcher


async def handle_create_branch(callback_query: types.CallbackQuery):
    """Handle create branch callback for superadmin."""
    await callback_query.answer("Форма для создания филиала открыта.")


async def handle_manage_users(callback_query: types.CallbackQuery):
    """Handle manage users callback for superadmin."""
    await callback_query.answer("Управление пользователями открыто.")


def register_superadmin_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(handle_create_branch, text="create_branch")
    dp.register_callback_query_handler(handle_manage_users, text="manage_users")
