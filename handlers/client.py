from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import genMenu



# @dp.message_handler(commands=['start'])
async def commands_start(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    try:
        await bot.send_message(message.from_user.id, 'Доброго времени суток, студенты!\n\
Вы находитесь в главном меню проекта GB_DreamTeam от одноименной команды.\n\
Выберете проект с которым ходите ознакомиться.', reply_markup=genMenu)
        await message.delete()
    except:
        await message.reply('Общение с ботом просьба осуществлять через личные сообщения к боту:\
             https://t.me/GB_DreamTeam_Project_bot')


# @dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'https://telegra.ph/EHkspediciya-10-13-3', reply_markup=genMenu)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_help, commands=['help'])
