from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from models.users import User
from filters import IsNewUser
from aiogram.fsm.context import FSMContext
from states import RegisterState
from msges import Message_contents
from aiogram.enums import ChatMemberStatus
from asyncio import sleep
from config import CHANNEL_ID, CHANNEL_URL
from keyboards import consultation_menu_ik, consultation_menu_rk
import re

router = Router()

# @router.message(RegisterState.WAITING_FOR_NAME)
# async def register_user_name(message: Message, state: FSMContext):
#     name = message.text
#     await state.update_data(name=name)
#     await message.answer(Message_contents.waiting_for_phone_number_prompt)
#     await state.set_state(RegisterState.WAITING_FOR_PHONE_NUMBER)

# @router.message(RegisterState.WAITING_FOR_PHONE_NUMBER)
# async def register_user_phone(message: Message, state: FSMContext):
#     phone_number = message.text.strip()
#     data = await state.get_data()
    
#     cleaned_number = re.sub(r'[^\d]', '', phone_number)
#     if cleaned_number.startswith('998'):
#         cleaned_number = cleaned_number[3:]
    
#     if len(cleaned_number) != 9:
#         await message.answer(
#             "Telefon raqam noto'g'ri formatda.\n"
#             "Quyidagi formatlardan birida kiriting:\n"
#             "• +998901234567\n"
#             "• 998901234567\n"
#             "• 901234567\n"
#             "• 90 123 45 67\n"
#             "• +998 90 123 45 67"
#         )
#         return
    
#     valid_codes = ['90', '91', '93', '94', '95', '97', '98', '99', '33', '88', '20', '50', '55', '56', '58']
#     operator_code = cleaned_number[:2]
    
#     if operator_code not in valid_codes:
#         await message.answer(
#             "Telefon raqam O'zbekiston operatorlariga mos emas.\n"
#             "Iltimos, to'g'ri telefon raqamni kiriting."
#         )
#         return
    
#     formatted_number = f"+998 {cleaned_number[:2]} {cleaned_number[2:5]} {cleaned_number[5:7]} {cleaned_number[7:9]}"
    
#     name = data.get("name")

#     user = await User.create(
#         telegram_id=str(message.from_user.id),
#         name=name,
#         phone_number=formatted_number
#     )

#     await message.answer(Message_contents.registration_complete, parse_mode="HTML")
    
#     await message.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5165396993, message_id=569)
#     await message.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5165396993, message_id=575, caption="""
# 🏆 Noldan 3 oyda B1 olgan Farangizning hikoyasi

# – Qanday boshlagani
# – Nimalar bilan shugʻullangani
# – Qanday shugʻullangani

# 📈VA 2 oylik natija beruvchi roadmap!

# Albatta ko'ring, ingliz tilini o'rganish haqida fikrlaringiz butunlay o'zgarib ketadi✅

# (Ayni shunga moslangan siz uchun individual bepul konsultatsiya olish uchun "Konsultatsiya olish" tugmasini bosing)
# """)
    
    
#     await state.clear()
#     await sleep(3600)
#     await message.answer_photo(photo=FSInputFile("image.png"), caption=Message_contents.consult_msg, reply_markup=consultation_menu_ik, parse_mode="HTML")

@router.message(IsNewUser())
async def register_user_start(message: Message, state: FSMContext):
    # await message.answer(Message_contents.waiting_for_name_prompt)
    # await state.set_state(RegisterState.WAITING_FOR_NAME)

    user = await User.create(
        telegram_id=str(message.from_user.id),
        name=message.from_user.full_name,
        phone_number="kiritlmagan"
    )

    await message.answer(Message_contents.registration_complete, parse_mode="HTML")
    
    await message.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5165396993, message_id=12)
    await message.bot.copy_message(chat_id=message.from_user.id, from_chat_id=5165396993, message_id=16, caption="""
🏆 Noldan 3 oyda B1 olgan Farangizning hikoyasi

– Qanday boshlagani
– Nimalar bilan shugʻullangani
– Qanday shugʻullangani

📈VA 2 oylik natija beruvchi roadmap!

Albatta ko'ring, ingliz tilini o'rganish haqida fikrlaringiz butunlay o'zgarib ketadi✅

(Ayni shunga moslangan siz uchun individual bepul konsultatsiya olish uchun "Konsultatsiya olish" tugmasini bosing)
""")
    
    
    await state.clear()
    await sleep(3600)
    await message.answer_photo(photo=FSInputFile("image.png"), caption=Message_contents.consult_msg, reply_markup=consultation_menu_ik, parse_mode="HTML")


@router.callback_query(F.data == "check_subscribe")
async def check_subscription(callback_query: CallbackQuery, state: FSMContext):
    member = await callback_query.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback_query.from_user.id)
    if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        user = await User.get_or_none(telegram_id=str(callback_query.from_user.id))
        if not user:
            await callback_query.message.answer(Message_contents.waiting_for_name_prompt)
            await state.set_state(RegisterState.WAITING_FOR_NAME)
        else:
            await callback_query.message.answer(Message_contents.already_registered)
        await callback_query.answer("Obunangiz tasdiqlandi!", show_alert=True)
        await callback_query.message.delete()
    else:
        await callback_query.answer("Iltimos, kanalga obuna bo'ling va qayta tekshiring.", show_alert=True)

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer(Message_contents.already_registered)
