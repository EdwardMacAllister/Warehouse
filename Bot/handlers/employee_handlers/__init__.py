from aiogram import Dispatcher

from .orders_handler import register_order_handlers
from .employee_management import register_employee_handlers
from .sales_handler import register_sales_handlers


def register_admin_commands(dp: Dispatcher):
    register_order_handlers(dp)
    register_employee_handlers(dp)
    register_sales_handlers(dp)
