from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

price_btn = KeyboardButton('Прайс💵')
place_btn = KeyboardButton('Где мы находимся?📌')
tour_btn = KeyboardButton('Турниры🏆')
call_admin = KeyboardButton('Позвать админа')
otz_btn = KeyboardButton('Оставить отзыв')
akcii_btn = KeyboardButton('Акции🎁')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(price_btn,place_btn).row(akcii_btn, tour_btn).row(call_admin, otz_btn)
