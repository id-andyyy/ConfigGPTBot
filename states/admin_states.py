from aiogram.filters.state import State, StatesGroup


class FSMAddUser(StatesGroup):
    forward_message = State()
