from aiogram import Router
from aiogram.types import Message

router: Router = Router()


@router.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)
