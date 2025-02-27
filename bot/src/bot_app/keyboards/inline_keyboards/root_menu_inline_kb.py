from enum import auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot_app.utils.common import CustomEnumAuto


class RootMenuActions(CustomEnumAuto):
    notifications = auto()
    contacts = auto()
    schedules = auto()


class RootMenuCbData(CallbackData, prefix='root_menu'):
    action: str


def root_menu_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    labels = ['Оповещения', 'Контакты', 'Расписания']

    for i, action in enumerate(RootMenuActions):
        b.button(text=labels[i], callback_data=RootMenuCbData(action=action).pack())

    b.adjust(1)
    return b.as_markup()
