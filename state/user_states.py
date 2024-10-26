# states/user_states.py
from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    waiting_for_username_password = State()  # For registration and login
