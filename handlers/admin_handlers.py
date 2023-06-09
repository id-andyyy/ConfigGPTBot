from aiogram import F
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from lexicon.lexicon_ru import *
from states.admin_states import FSMAddUser

router: Router = Router()


@router.message(Command(commands='adduser'))
async def process_adduser_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_ADMIN['/adduser'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMAddUser.forward_message)


@router.message(StateFilter(FSMAddUser.forward_message))
async def process_message_forwarded(message: Message, state: FSMContext):
    if message.forward_from is not None:
        await message.answer(text=LEXICON_ADMIN['user_added'].format(name=message.forward_from.first_name))
    else:
        await message.answer(text=LEXICON_ADMIN['incorrect_message'])
    await state.clear()
