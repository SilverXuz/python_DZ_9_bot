from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# b1 = KeyboardButton('❌ Крестики-нолики ⭕')
kb1 = KeyboardButton('1️⃣')
kb2 = KeyboardButton('2️⃣')
kb3 = KeyboardButton('3️⃣')
kb4 = KeyboardButton('4️⃣')
kb5 = KeyboardButton('5️⃣')
kb6 = KeyboardButton('6️⃣')
kb7 = KeyboardButton('7️⃣')
kb8 = KeyboardButton('8️⃣')
kb9 = KeyboardButton('9️⃣')
btnEndGame_xo = KeyboardButton('🔙 Выход')

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_input_xo = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client.add(b1)
kb_input_xo.add(kb1, kb2, kb3).add(kb4, kb5, kb6).add(kb7, kb8, kb9).add(btnEndGame_xo)
