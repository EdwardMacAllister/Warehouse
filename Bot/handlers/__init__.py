# handlers/__init__.py

from aiogram import Dispatcher
from .admin import register_admin_handlers  # Register admin handlers
from .auth import register_auth_handlers  # Ensure this matches the actual handler name
from .user import register_user_handlers  # Make sure this matches the defined function
from .main_screen import register_screen_handlers  # Register main screen handlers


def register_all_handlers(dp: Dispatcher):
    """Register all handlers in the bot."""
    register_admin_handlers(dp)  # Register admin handlers
    register_auth_handlers(dp)  # Register auth handlers (previously 'employee_handlers')
    register_user_handlers(dp)  # Register user handlers
    register_screen_handlers(dp)  # Register main screen handlers
