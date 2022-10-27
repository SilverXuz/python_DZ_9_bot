from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_candy, kb_konfeta_end, genMenu

candy = 81     # Общее количество конфет

# @dp.message_handler(commands=['🍭 Конфеты'])
async def command_place(message: types.Message):
    print(f'Игрок {message.from_user.full_name} играет в 🍭 Конфеты!')
    await bot.send_message(message.from_user.id, "Правила игры:\n\
Игрок и бот по очереди берут из кучки от 1 до 8 конфет за раз. \
    Побеждает тот, кто заберет последние конфеты из кучки. Всего в кучке 81 конфеты.", reply_markup=kb_candy)
    global candy
    if candy < 81:
        candy = 81

# @dp.message_handler(Text=['1'])
async def text1(message: types.Message):
    
    global candy
    if candy <= 0:
        candy == 81
    candy -= int(message.text)
    await message.reply(f'Осталось {candy} конфет')
    
    if candy <= 0:
        await message.answer('Игрок победил', reply_markup=kb_konfeta_end)
        candy = 81
        
        
    elif 7 >= candy > 0:    
        await message.answer(f'Бот взял {candy} конфет.\nБот победил', reply_markup=kb_konfeta_end)
        candy = 81
        
    else:
        candy -= (9 - int(message.text))
        await message.answer(f'Бот взял {9 - int(message.text)} конфет.')
        await message.answer(f'Осталось {candy} конфет')


# Кнопка Сыграть снова
async def reload_game(message: types.Message):
    await command_place(message)



# Кнопка 🔙 Выход
async def text_back(message : types.Message):
    await bot.send_message(message.from_user.id, 'Попробуйте другие первоклассные проекты!', reply_markup=genMenu)


def register_handlers_konfeta(dp: Dispatcher):
    dp.register_message_handler(command_place, text=['🍭 Конфеты'])
    dp.register_message_handler(text1, text=['1'])
    dp.register_message_handler(text1, text=['2'])
    dp.register_message_handler(text1, text=['3'])
    dp.register_message_handler(text1, text=['4'])
    dp.register_message_handler(text1, text=['5'])
    dp.register_message_handler(text1, text=['6'])
    dp.register_message_handler(text1, text=['7'])
    dp.register_message_handler(text1, text=['8'])
    dp.register_message_handler(reload_game, text=['Сыграть снова'])
    dp.register_message_handler(text_back, text=['🔙 Выход'])
