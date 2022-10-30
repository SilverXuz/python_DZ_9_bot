from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

c1 = KeyboardButton('1🍭')
c2 = KeyboardButton('2🍭')
c3 = KeyboardButton('3🍭')
c4 = KeyboardButton('4🍭')
c5 = KeyboardButton('5🍭')
c6 = KeyboardButton('6🍭')
c7 = KeyboardButton('7🍭')
c8 = KeyboardButton('8🍭')


btnReload = KeyboardButton('Сыграть снова')
btnEndGame = KeyboardButton('🔙 Выход 🍭')


kb_candy = ReplyKeyboardMarkup(resize_keyboard=True)
kb_candy.row(c1, c2, c3, c4). row(c5, c6, c7, c8).row(btnEndGame)

kb_konfeta_end = ReplyKeyboardMarkup(resize_keyboard=True)
kb_konfeta_end.add(btnReload).add(btnEndGame)
