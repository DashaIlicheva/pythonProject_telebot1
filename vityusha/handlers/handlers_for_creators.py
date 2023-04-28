from aiogram import Router, F
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram.filters import Text, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from vityusha.lexicon.lexicon_vit import LEXICON_CREATORS

router: Router = Router()
redis: Redis = Redis(host='localhost')
storage: RedisStorage = RedisStorage(redis=redis)


class FSMFillAForm(StatesGroup):
    form_name_cr = State()
    class_cr = State()
    num_of_mat_cr = State()
    matter_cr = State()
    answer_cr = State()
    choice_cr = State()


@router.callback_query(Text(text='make'), StateFilter(default_state))
async def process_make_bt(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=LEXICON_CREATORS['name_form'])
    await state.set_state(FSMFillAForm.form_name_cr)


@router.message(StateFilter(FSMFillAForm.form_name_cr))
async def class_cr(msg: Message, state: FSMContext):
    await msg.answer(text=LEXICON_CREATORS['class'])
    await state.set_state(FSMFillAForm.class_cr)


