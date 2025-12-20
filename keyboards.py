from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

consultation_menu_rk = ReplyKeyboardBuilder()
consultation_menu_rk.button(text="🔥 Konsultatsiya olish")
consultation_menu_rk = consultation_menu_rk.as_markup(resize_keyboard=True)

consultation_menu_ik = InlineKeyboardBuilder()
consultation_menu_ik.button(text="🔥 Konsultatsiya olish", callback_data="consultation")
consultation_menu_ik = consultation_menu_ik.as_markup()