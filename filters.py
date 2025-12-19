from aiogram.filters import Filter
from models.users import User
from aiogram.types import Message
from config import ADMIN_ID

class IsNewUser(Filter):
    async def __call__(self, message: Message) -> bool:
        user = await User.get_or_none(telegram_id=str(message.from_user.id))
        return user is None and message.from_user.id != ADMIN_ID