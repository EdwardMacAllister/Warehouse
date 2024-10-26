# states/superadmin_states.py
from aiogram.fsm.state import StatesGroup, State


class SuperAdminStates(StatesGroup):
    waiting_for_branch_info = State()  # Waiting for branch creation info
    updating_branch = State()  # Waiting for branch update info
    deleting_branch = State()  # Waiting for branch ID input to delete
