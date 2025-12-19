from aiogram import Bot
from aiogram.types import Message
from models.users import User
from models.admin import Post, ViewsPosts
from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter
from datetime import datetime, timedelta, timezone
from aiogram.utils.keyboard import InlineKeyboardBuilder
import msges
import asyncio

async def send_posts_task(bot: Bot):
    while True:
        users = await User.all()
        scheduled_posts = await Post.all()
        for user in users:
            for post in scheduled_posts:
                now = datetime.now(timezone.utc)
                send_at = user.created_at + post.send_time - timedelta(minutes=1)
                
                if send_at <= now:
                    already_viewed = await ViewsPosts.filter(post=post, user_telegram_id=user.telegram_id).first()
                    if not already_viewed:
                        try:
                            msg = await bot.copy_message(chat_id=int(user.telegram_id), from_chat_id=post.from_chat_id, message_id=post.message_id)
                            await ViewsPosts.create(post=post, user_telegram_id=user.telegram_id, message_id=msg.message_id)
                        except TelegramForbiddenError:
                            await user.delete()
                        except TelegramRetryAfter as e:
                            await asyncio.sleep(e.retry_after)
                        except Exception as e:
                            print(f"Error sending post to user {user.telegram_id}: {e}")
                    elif already_viewed.viewed_at + timedelta(days=1) <= now:
                        try:
                            await bot.delete_message(chat_id=int(user.telegram_id), message_id=already_viewed.message_id)
                        except TelegramForbiddenError:
                            await user.delete()
                        except TelegramRetryAfter as e:
                            await asyncio.sleep(e.retry_after)
                        except Exception as e:
                            print(f"Error deleting old post for user {user.telegram_id}: {e}")
        await asyncio.sleep(10)