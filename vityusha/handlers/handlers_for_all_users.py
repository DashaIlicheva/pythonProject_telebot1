import asyncio
from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from vityusha.lexicon.lexicon_vit import LEXICON_COMMANDS
from vityusha.keyboards.keyboards import start_keyboard

router: Router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def send_start(msg: Message):
    await msg.answer(text=LEXICON_COMMANDS['/start'],
                     reply_markup=await start_keyboard())


@router.message(Command(commands='help'))
async def send_help(msg: Message):
    await msg.answer(text=LEXICON_COMMANDS['/help'])


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def cancel_on(msg: Message, state: FSMContext):
    await msg.answer(text=LEXICON_COMMANDS['/cancel_on'])
    await state.clear()


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def cancel_off(msg: Message, state: FSMContext):
    await msg.answer(text=LEXICON_COMMANDS['/cancel_off'])
