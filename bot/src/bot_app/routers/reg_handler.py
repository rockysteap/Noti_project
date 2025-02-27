import re

from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.bot_app.states.reg_states import RegStates
# from src.bot_app.keyboards.reg_kb import REG_TEXT

router = Router()
#
#
# @router.message(F.text == REG_TEXT)
# async def register_init(message: Message, state: FSMContext):
#     await state.clear()
#
#     await state.set_state(RegStates.reg_name)
#     await message.answer(f'Введите имя, как к вам обращаться?')
#
#
# @router.message(RegStates.reg_name)
# async def register_name(message: Message, state: FSMContext):
#     await state.update_data(reg_name=message.text)
#     print(await state.get_data())
#     await state.set_state(RegStates.reg_phone)
#     await message.answer(f'Введите номер телефона')
#
#
# @router.message(RegStates.reg_phone)
# async def register_phone(message: Message, state: FSMContext):
#     if re.findall(r'[+]?\d[ ]?[(]?\d{3}[)]?[ ]?\d{2,3}[- ]?\d{2}[- ]?\d{2}', message.text):
#         await state.update_data(reg_phone=message.text)
#         data = await state.get_data()
#         print(await state.get_data())
#         await message.answer(f'Успешная регистрация, имя: {data["reg_name"]}, телефон: {data["reg_phone"]}')
#         await state.clear()
#     else:
#         await message.answer(f'Указанный номер не подходит, пожалуйста, повторите')
