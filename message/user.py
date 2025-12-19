from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from models.users import User
from filters import IsNewUser
from aiogram.fsm.context import FSMContext
from states import RegisterState
from msges import Message_contents
from asyncio import sleep
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re

router = Router()

@router.message(RegisterState.WAITING_FOR_NAME)
async def register_user_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(Message_contents.waiting_for_phone_number_prompt)
    await state.set_state(RegisterState.WAITING_FOR_PHONE_NUMBER)

@router.message(RegisterState.WAITING_FOR_PHONE_NUMBER)
async def register_user_phone(message: Message, state: FSMContext):
    phone_number = message.text.strip()
    data = await state.get_data()
    
    cleaned_number = re.sub(r'[^\d]', '', phone_number)
    if cleaned_number.startswith('998'):
        cleaned_number = cleaned_number[3:]
    
    if len(cleaned_number) != 9:
        await message.answer(
            "Telefon raqam noto'g'ri formatda.\n"
            "Quyidagi formatlardan birida kiriting:\n"
            "• +998901234567\n"
            "• 998901234567\n"
            "• 901234567\n"
            "• 90 123 45 67\n"
            "• +998 90 123 45 67"
        )
        return
    
    valid_codes = ['90', '91', '93', '94', '95', '97', '98', '99', '33', '88', '20', '50', '55', '56', '58']
    operator_code = cleaned_number[:2]
    
    if operator_code not in valid_codes:
        await message.answer(
            "Telefon raqam O'zbekiston operatorlariga mos emas.\n"
            "Iltimos, to'g'ri telefon raqamni kiriting."
        )
        return
    
    formatted_number = f"+998 {cleaned_number[:2]} {cleaned_number[2:5]} {cleaned_number[5:7]} {cleaned_number[7:9]}"
    
    name = data.get("name")

    user = await User.create(
        telegram_id=str(message.from_user.id),
        name=name,
        phone_number=formatted_number
    )

    await message.answer(Message_contents.registration_complete)
    await state.clear()
    await sleep(60)
    markup = InlineKeyboardBuilder().button(text="🔥 Konsultatsiya olish", url="https://tally.so/r/rjDzXX").as_markup()
    await message.answer_photo(photo=FSInputFile("image.png"), caption=Message_contents.consult_msg, reply_markup=markup, parse_mode="HTML")

@router.message(IsNewUser())
async def register_user_start(message: Message, state: FSMContext):
    await message.answer(Message_contents.waiting_for_name_prompt)
    await state.set_state(RegisterState.WAITING_FOR_NAME)

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer(Message_contents.already_registered)
