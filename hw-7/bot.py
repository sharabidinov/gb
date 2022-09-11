import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from get_content import get_content
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
lang = 'ru/'
section_list, subsection_list, questions, answers = None, None, None, None
languages = ['🇰🇬 Кыргызча', '🇷🇺 Русский']


@dp.message_handler(commands=['start'])
@dp.message_handler(text=['На главную'])
async def start_command(message: types.Message):
    text = '''- Саламатсыздарбы! Форевер Ливинг Продактс КР компаниясынын колдоо кызматына кош келиниздер!\n
- Добрый день! Добро пожаловать в службу поддержки  ОсОО «Форевер Ливинг Продактс КР»'''
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(*(types.KeyboardButton(language) for language in languages))
    await message.answer(text, reply_markup=keyboard)


@dp.message_handler(text=languages)
async def section_message_handler(message: types.Message):
    reply_action_message = message.text
    global lang
    if reply_action_message == '🇷🇺 Русский':
        lang = 'ru/'
        reply_text = 'Выберите раздел'
    elif reply_action_message == '🇰🇬 Кыргызча':
        lang = 'ky/'
        reply_text = 'Бөлүмдү тандаңыз'
    global section_list, subsection_list, questions, answers
    section_list, subsection_list, questions, answers = get_content(lang)
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    keyboard.add(*(types.KeyboardButton(section_button)
                   for section_button in section_list))
    await message.answer(reply_text, reply_markup=keyboard)


@dp.message_handler()
async def subsection_message_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    for item in section_list:
        if message.text == section_list[section_list.index(item)]:
            keyboard.add(*(types.KeyboardButton(button) for button in subsection_list if button[:2] in section_list[
                section_list.index(item)]))
            keyboard.row('На главную')
            if lang == 'ru/':
                reply_text = 'Выберите подраздел'
            else:
                reply_text = 'Бөлүмдү тандаңыз'
            await message.answer(reply_text, reply_markup=keyboard)
    for _ in questions:
        answer_html = list(filter(lambda c: c[0] == message.text, answers))
        if answer_html:
            await message.answer(answer_html[0][1])
            for i in answer_html[0][2]:
                await message.answer_photo(i.get('src'))
            break


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
