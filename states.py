from aiogram.dispatcher.filters.state import State, StatesGroup

class User(StatesGroup):
    contact_state = State()
    choice_state = State()
    group_state = State()