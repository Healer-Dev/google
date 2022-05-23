# Birinchi kutubxona import qilib olamiz

from googlesearch import search
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

# Endi bot sozlamalari

logging.basicConfig(level = logging.INFO)
bot = Bot(token = '5349342778:AAFvZmqcYeYwRLZrac7Hb3bB7RzC1BmxUqQ')
dp = Dispatcher(bot)

# Quyida javob qaytaruvchi tugmalar

al = KeyboardButton('Rasmlar')
ai = KeyboardButton('Barchasi')
kbs = ReplyKeyboardMarkup(resize_keyboard=True).add(al,ai)

# Bu funksiya foydalanuvchidan start kommandasi kelsa ishlaydi

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.first_name}\nMen Google Qidiruv botiman qidirmoqchi bo'lgan so'rovni kiriting:\nBot yaratuvchisi @healer_ghost_riley")

aut = []

# Bu funksiya foydalanuvchidan Rasmlar xabari kelsa ishlaydi

@dp.message_handler(text = 'Rasmlar')
async def echo(message: types.Message):
    for p in aut:
        await message.answer_photo(p,reply_markup = ReplyKeyboardRemove())
    aut.clear()

# Bu funksiya foydalanuvchidan Barchasi xabari kelsa ishlaydi

@dp.message_handler(text = 'Barchasi')
async def echo(message: types.Message):
    for e in (aut[:10]):
        await message.answer(e,reply_markup = ReplyKeyboardRemove())
    aut.clear()

# Bu umumiy xabar filteri

@dp.message_handler()
async def echo(message: types.Message):
    for i in search(message.text,stop = 25):
        aut.append(i)
    await message.reply("Qanday Turdagi Malumot Kerak",reply_markup = kbs)

# Quyida botni ishlatuvchi kodlar

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)