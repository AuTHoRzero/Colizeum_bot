##############
##Библиотеки##
##############
import asyncio
import logging
import keyboard as keyboard
from aiogram.types import InputFile
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.helper import Helper, HelperMode, ListItem


###############
##Логирование##
###############
logging.basicConfig(level=logging.INFO)

###############
##Объект бота##
###############
bot = Bot(token='')

############################
##Диспетчер(Для хэндлеров)##
############################
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Hello', reply_markup = keyboard.main_menu)

@dp.message_handler(text= ['Прайс💵'] )
async def price(message:types.Message):
    await bot.send_photo(message.from_user.id, 'https://sun9-82.userapi.com/impg/KT3LEAEgkkTx920JtJv1ojs09OSgSNaZbCgDEA/25aNHnh8-vQ.jpg?size=720x1280&quality=96&sign=2a1c5bde2600ef3c538b8635d164eb87&type=album')

@dp.message_handler(text= ['Где мы находимся?📌'] )
async def place(message:types.Message):
    await message.answer('📌Наш адрес: Малый просп. Васильевского острова, 88, корп. 2, Санкт-Петербургэтаж 4\n📱Телефон:+7 (905) 236-18-84\n⏰Работаем круглосуточно, 24/7!')
    await bot.send_location(message.from_user.id, 59.938748, 30.229163)


@dp.message_handler(text= ['Турниры🏆'] )
async def tournament(message:types.Message):
    await bot.send_photo(message.from_user.id, 'https://sun9-72.userapi.com/impg/za3Nzw1zDjkUMq0FE84XBP5HeOUi3vTFso9MUQ/Q_597ZYUFkA.jpg?size=2560x1439&quality=96&sign=50abcdf6a4a84ae6ab6699d530d71ee3&type=album', caption='Каждый месяц вы можете участвовать в наших турнирах🏆, вот список на Декабрь❄')

@dp.message_handler(text= ['Оставить отзыв'] )
async def review (message:types.Message):
    await message.answer('😉⚫😉\nОставь отзывы перейдя по ссылке.\n🟡😎🟡\n\nВк:\nhttps://vk.com/topic-207016376_48071555\n2ГИС:\nhttps://2gis.ru/spb/firm/70000001059088854/tab/reviews\nЯндекс:\nhttps://yandex.ru/maps/org/colizeum_primorskaya/113216891152/reviews/?ll=30.229162,59.938748&z=16\nGoogle:\nhttps://www.google.ru/maps/place/COLIZEUM+CLUB+Приморская/@59.938291,30.2284791,17z/data=!4m7!3m6!1s0x469637f765112135:0x600878ac666f7194!8m2!3d59.938291!4d30.2306731!9m1!1b1')

@dp.message_handler(text= ['Позвать админа'] )
async def call_admin (message:types.Message):
    await message.answer('Проверь, чтобы у тебя был указан Юзернейм, администратор скоро напишет')
#    await bot.answer (f'{message.from_user.id}\n{message.from_user.username}')
    await bot.send_message ( '5054595026' , f'Новое сообщение от:  @{message.from_user.username}')

@dp.message_handler(text= ['Акции🎁'] )
async def akcii (message:types.Message):
    await message.answer('Список актуальных акций можно найти тут, проверяй почаще, мы любим радовать вас чем-то новым😘\nhttps://telegra.ph/Akcii-Colizeum-Primorskaya-12-15')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
