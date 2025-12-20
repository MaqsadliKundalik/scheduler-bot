from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from models.users import User

router = Router()

@router.message(F.text == "🔥 Konsultatsiya olish")
async def consultation_request(message: Message):
    await message.answer()