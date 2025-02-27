from aiogram.fsm.state import StatesGroup, State


class RegStates(StatesGroup):
    reg_name = State()
    reg_phone = State()
