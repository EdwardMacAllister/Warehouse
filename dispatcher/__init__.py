from aiogram import Dispatcher

from .routers.auth_router import auth_router
from .routers.admin_router import admin_router
from .routers.superadmin_router import superadmin_router


def register_all_routers(dp: Dispatcher):
    """Register all routers in the dispatcher."""
    dp.include_router(auth_router)
    dp.include_router(admin_router)
    dp.include_router(superadmin_router)
