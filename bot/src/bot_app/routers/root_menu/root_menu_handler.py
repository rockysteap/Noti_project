from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.bot_app.keyboards.inline_keyboards.root_menu_inline_kb import RootMenuActions, RootMenuCbData

router = Router(name=__name__)


@router.callback_query(RootMenuCbData.filter(F.action == RootMenuActions.contacts.value))
# @router.callback_query(RootMenuCbData.filter(F.action == 'contacts'))
async def handle_root_menu_contacts(call: CallbackQuery):
    await call.message.answer('Контакты в работе')


@router.callback_query(RootMenuCbData.filter(F.action == RootMenuActions.notifications.value))
async def handle_root_menu_contacts(call: CallbackQuery):
    await call.message.answer('Оповещения в работе')


@router.callback_query(RootMenuCbData.filter(F.action == RootMenuActions.schedules.value))
async def handle_root_menu_contacts(call: CallbackQuery):
    await call.message.answer('Расписания в работе')
