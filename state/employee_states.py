# states/employee_states.py
from aiogram.fsm.state import StatesGroup, State


class EmployeeStates(StatesGroup):
    waiting_for_info = State()  # State for waiting for user input
    view_inventory = State()  # State for viewing inventory
    generate_report = State()  # State for generating reports
