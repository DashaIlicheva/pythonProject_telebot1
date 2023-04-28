from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from vityusha.lexicon.lexicon_vit import LEXICON_BUTTON


async def start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text=LEXICON_BUTTON['make'], callback_data='make'),
           InlineKeyboardButton(text=LEXICON_BUTTON['pass'], callback_data='pass'),
           width=2)
    return kb.as_markup()

