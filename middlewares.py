from aiogram import BaseMiddleware
from config import CHANNEL_ID, CHANNEL_URL
from aiogram.types import Message
from aiogram.enums import ChatMemberStatus
from aiogram.utils.keyboard import InlineKeyboardBuilder
from msges import Message_contents

class CheckSUbChannelMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        try:
            member = await event.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=event.from_user.id)
            chat = await event.bot.get_chat(CHANNEL_ID)
            markup = InlineKeyboardBuilder()
            markup.button(
                text=chat.title,
                url=CHANNEL_URL
            )
            markup.button(
                text="✅ Obunani tekshirish",
                callback_data="check_subscribe"
            )
            markup = markup.as_markup()
            if member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]:
                
                await event.answer(
                    Message_contents.check_sub_msg,
                    reply_markup=markup 
                )
                return
        except Exception as e:
            print(f"Error checking channel membership: {e}")
            await event.answer(
                Message_contents.check_sub_msg,
                reply_markup=InlineKeyboardBuilder().button(
                    text="🔔 Obuna bo'lish",
                    url=CHANNEL_URL
                ).as_markup()
            )
            return

        return await handler(event, data)