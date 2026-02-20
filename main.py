import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram import F  # новый импорт!
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # новый импорт!
from variables import *

import os
from aiohttp import web

TOKEN = os.getenv('BOT_TOKEN')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---------------

async def handle(request):
    return web.Response(text="Bot is running!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render сам подставит порт в переменную среды PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# --------------

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(helo)


@dp.message(Command('songs'))
async def cmd_songs(message: Message):
    builder = ReplyKeyboardBuilder()

    for song in demo_list:
        builder.add(types.KeyboardButton(text=song))
    builder.adjust(2)
    await message.answer('Выберите число:', reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(Command('full_text'))
async def cmd_full(message: Message):
    builder = ReplyKeyboardBuilder()

    for song in demo_list:
        builder.add(types.KeyboardButton(text=song+' - текст'))
    builder.adjust(2)
    await message.answer('Выберите число:', reply_markup=builder.as_markup(resize_keyboard=True))



@dp.message(Command('release'))
async def cmd_release(message: Message):
    await message.answer(https_release)


@dp.message(F.text == 'RED FLAG')
async def btn_red(message: Message):
    #await message.answer(text_song_RED_FLAG)
    image = FSInputFile(img_RED_FLAG)
    await message.answer_photo(image, caption=text_song_RED_FLAG2, reply_markup=types.ReplyKeyboardRemove())
     # , reply_markup=types.ReplyKeyboardRemove() - удалить клаву
    
@dp.message(F.text == 'RED FLAG - текст')
async def btn_red2(message: Message):
    await message.answer(text_song_RED_FLAG)

@dp.message(F.text == 'ИНДУСТРИЯ')
async def btn_indastry(message: Message):
    # await message.answer(text_song_INDUSTRIA)
    image = FSInputFile(img_INDUSTRIA)
    await message.answer_photo(image, caption = text_song_INDUSTRIA, reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == 'ИНДУСТРИЯ - текст')
async def btn_indastry2(message: Message):
    await message.answer(text_song_INDUSTRIA)


@dp.message(F.text == 'ARMANI')
async def btn_armani(message: Message):
    image = FSInputFile(img_ARMANI)
    await message.answer_photo(image, caption = text_song_ARMANI2, reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == 'ARMANI - текст')
async def btn_armani2(message: Message):
    await message.answer(text_song_ARMANI, reply_markup=types.ReplyKeyboardRemove())



@dp.message(F.text == 'БИПОЛЯРКА - текст')
async def btn_bipolarka2(message: Message):
    # await message.answer(text_song_BIPOLARKA)
    image = FSInputFile(img_BIPOLARKA)
    await message.answer_photo(image, caption=text_song_BIPOLARKA, reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == 'БРЕЗГЛИВОСТЬ')
async def btn_brezglivost(message: Message):
    image = FSInputFile(img_BREZGLIVOST)
    await message.answer_photo(image, caption=text_song_BREZLIVOST, reply_markup=types.ReplyKeyboardRemove())

async def main():
    await start_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



