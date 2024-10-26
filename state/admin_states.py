# states/admin_states.py
from aiogram.fsm.state import StatesGroup, State


class AdminStates(StatesGroup):
    add_user = State()  # Waiting for username input when adding a user
    password = State()  # Waiting for password input
    remove_user = State()  # Waiting for username input when removing a user
