from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import genMenu, kb_input_xo
import random


# Функция которая отвечает на команду ❌ Крестики-нолики ⭕
async def start_game_xo(message: types.Message):
    print(f'Игрок {message.from_user.full_name} играет в ❌ Крестики-нолики ⭕!')
    await bot.send_message(message.from_user.id, 'Игра находится на этапе разработки и работает не корректно!', reply_markup=kb_input_xo)
    await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)


async def to_game(message: types.Message):
    if message.text == '1️⃣': await bot.send_message(message.from_user.id, '❌🔲🔲\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo) 
    elif message.text == '2️⃣': await bot.send_message(message.from_user.id, '🔲❌🔲\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '3️⃣': await bot.send_message(message.from_user.id, '🔲🔲❌\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '4️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n❌🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '5️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲❌🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '6️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲❌\n🔲🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '7️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n❌🔲🔲', reply_markup=kb_input_xo)
    elif message.text == '8️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n🔲❌🔲', reply_markup=kb_input_xo)
    elif message.text == '9️⃣': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n🔲🔲❌', reply_markup=kb_input_xo)
    busy = []
    busy.append(message.text)
    bot_move = str(random.randint(1, 9)) 
    while bot_move in busy:
        print(bot_move)
        bot_move = str(random.randint(1, 9)) 
    else:
        if bot_move == '1': await bot.send_message(message.from_user.id, '⭕🔲🔲\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo) 
        elif bot_move == '2': await bot.send_message(message.from_user.id, '🔲⭕🔲\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '3': await bot.send_message(message.from_user.id, '🔲🔲⭕\n🔲🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '4': await bot.send_message(message.from_user.id, '🔲🔲🔲\n⭕🔲🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '5': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲⭕🔲\n🔲🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '6': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲⭕\n🔲🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '7': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n⭕🔲🔲', reply_markup=kb_input_xo)
        elif bot_move == '8': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n🔲⭕🔲', reply_markup=kb_input_xo)
        elif bot_move == '9': await bot.send_message(message.from_user.id, '🔲🔲🔲\n🔲🔲🔲\n🔲🔲⭕', reply_markup=kb_input_xo)


# Кнопка 🔙 Выход
async def text_back(message : types.Message):
    await bot.send_message(message.from_user.id, 'Попробуйте другие первоклассные проекты!', reply_markup=genMenu)


def register_handlers_krest_null(dp: Dispatcher):
    dp.register_message_handler(start_game_xo, text=['❌ Крестики-нолики ⭕️'])
    dp.register_message_handler(to_game, text=['1️⃣'])
    dp.register_message_handler(to_game, text=['2️⃣'])
    dp.register_message_handler(to_game, text=['3️⃣'])
    dp.register_message_handler(to_game, text=['4️⃣'])
    dp.register_message_handler(to_game, text=['5️⃣'])
    dp.register_message_handler(to_game, text=['6️⃣'])
    dp.register_message_handler(to_game, text=['7️⃣'])
    dp.register_message_handler(to_game, text=['8️⃣'])
    dp.register_message_handler(to_game, text=['9️⃣'])
    dp.register_message_handler(text_back, text=['🔙 Выход'])