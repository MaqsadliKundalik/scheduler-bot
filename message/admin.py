from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from models.users import User
from models.admin import Post
from config import ADMIN_ID
from aiogram.fsm.context import FSMContext
from states import PostCommandState, ScheduleState
from asyncio import sleep
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re
from openpyxl import Workbook
import os
from datetime import datetime, timedelta

router = Router()

@router.message(F.text == "/post")
async def admin_post_command(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("Iltimos, yubormoqchi bo'lgan xabaringizni kiriting.")
    await state.set_state(PostCommandState.WAITING_FOR_POST_CONTENT)

@router.message(PostCommandState.WAITING_FOR_POST_CONTENT)
async def handle_post_content(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    users = await User.all()
    await message.answer(f"Xabar {len(users)} foydalanuvchiga yuborilmoqda...")
    sent_count = 0
    for user in users:
        try:
            await message.bot.copy_message(chat_id=int(user.telegram_id), from_chat_id=message.chat.id, message_id=message.message_id)
            sent_count += 1
            await sleep(0.4)
        except Exception as e:
            print(f"Xatolik yuz berdi foydalanuvchi {user.telegram_id} ga xabar yuborishda: {e}")

    await message.answer(f"Xabar {sent_count}/{len(users)} foydalanuvchilarga yuborildi.")
    await state.clear()

@router.message(F.text == "/schedule")
async def admin_schedule_command(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("Xabarni yuboring.")
    await state.set_state(ScheduleState.WAITING_FOR_SCHEDULE_POST)

@router.message(ScheduleState.WAITING_FOR_SCHEDULE_POST)
async def handle_schedule_content(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("Xabar qachon yuborilsin?\n\nMasalan:\n• 1 kun 20 soat 30 minut\n• 2 soat\n• 30 minut\n• 1 kun")
    await state.update_data(post_content=message)
    await state.set_state(ScheduleState.WAITING_FOR_SCHEDULE_TIME)

@router.message(ScheduleState.WAITING_FOR_SCHEDULE_TIME)
async def handle_schedule_time(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    data = await state.get_data()
    post_content: Message = data.get("post_content")
    try:
        text = message.text.strip().lower()
        
        days = hours = minutes = 0

        day_match = re.search(r'(\d+)\s*kun', text)
        hour_match = re.search(r'(\d+)\s*soat', text)
        minute_match = re.search(r'(\d+)\s*minut', text)

        if day_match:
            days = int(day_match.group(1))
        if hour_match:
            hours = int(hour_match.group(1))
        if minute_match:
            minutes = int(minute_match.group(1))

        total_seconds = days * 86400 + hours * 3600 + minutes * 60
        if total_seconds <= 0:
            await message.answer("❌ Vaqt noto'g'ri!\n\nIltimos, kamida bitta qiymat kiriting:\n• 2 soat\n• 30 minut\n• 1 kun 5 soat")
            return

        from datetime import timedelta
        send_time = timedelta(seconds=total_seconds)
        
        await Post.create(
            from_chat_id=str(message.chat.id), 
            message_id=post_content.message_id, 
            send_time=send_time
        )
        
        time_parts = []
        if days > 0:
            time_parts.append(f"{days} kun")
        if hours > 0:
            time_parts.append(f"{hours} soat")
        if minutes > 0:
            time_parts.append(f"{minutes} minut")
        
        time_str = " ".join(time_parts)
        await message.answer(f"✅ Xabar saqlandi!\n\n⏰ Yuborilish vaqti: {time_str} ichida")
        
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {e}\n\nIltimos, vaqtni to'g'ri formatda kiriting.")

    await state.clear()

@router.message(F.text == "/scheduled_posts")
async def view_scheduled_posts(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    scheduled_posts = await Post.all().order_by('id')
    if not scheduled_posts:
        await message.answer("Hozircha rejalashtirilgan xabarlar yo'q.")
        return

    response_lines = ["Rejalashtirilgan xabarlar:"]
    for post in scheduled_posts:
        response_lines.append(f"/view{post.id} - {post.send_time}")

    await message.answer("\n".join(response_lines))

@router.message(F.text.startswith("/view"))
async def view_scheduled_post(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        post_id = int(message.text.replace("/view", "").strip())
        post = await Post.get(id=post_id)
        markup = InlineKeyboardBuilder().button(text="O'chirish", callback_data=f"delete_post_{post.id}").as_markup()
        await message.bot.copy_message(chat_id=message.chat.id, from_chat_id=post.from_chat_id, message_id=post.message_id)
        await message.answer(f"Xabarni o'chirasizmi?", reply_markup=markup)
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")

@router.callback_query(F.data.startswith("delete_post_"))
async def delete_scheduled_post(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.from_user.id != ADMIN_ID:
        return

    try:
        post_id = int(callback_query.data.replace("delete_post_", "").strip())
        post = await Post.get(id=post_id)
        await post.delete()
        await callback_query.message.edit_text("Xabar muvaffaqiyatli o'chirildi.")
    except Exception as e:
        await callback_query.message.answer(f"Xatolik yuz berdi: {e}")

@router.message(F.text == "/data")
async def export_users_to_excel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        users = await User.all().order_by('created_at')
        
        if not users:
            await message.answer("Hozircha foydalanuvchilar yo'q.")
            return
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Foydalanuvchilar"
        
        headers = ['№', 'ID', 'Telegram ID', 'Ism', 'Telefon raqam', 'Ro\'yxatdan o\'tgan sana']
        ws.append(headers)
        
        for cell in ws[1]:
            cell.font = cell.font.copy(bold=True)
        
        for idx, user in enumerate(users, start=1):
            ws.append([
                idx,
                user.id,
                user.telegram_id,
                user.name,
                user.phone_number or "Yo'q",
                user.created_at.strftime('%Y-%m-%d %H:%M:%S') if user.created_at else "Noma'lum"
            ])
        
        ws.column_dimensions['A'].width = 5
        ws.column_dimensions['B'].width = 8
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 30
        ws.column_dimensions['E'].width = 20
        ws.column_dimensions['F'].width = 20
        
        filename = f"users_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        filepath = os.path.join(os.getcwd(), filename)
        wb.save(filepath)
        
        await message.answer(f"📊 Jami foydalanuvchilar: {len(users)}")
        file = FSInputFile(filepath, filename=filename)
        await message.answer_document(file, caption=f"Foydalanuvchilar ro'yxati\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        os.remove(filepath)
        
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")

@router.message(F.text == "/check")
async def check_msg(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(F"Chat ID: {message.chat.id}\nMessage ID: {message.message_id}")