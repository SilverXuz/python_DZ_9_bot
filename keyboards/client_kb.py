from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры главного меню
btnCalc = KeyboardButton('🧮 Калькулятор')
btnKonfeta = KeyboardButton('🍭 Конфеты')
btnKN = KeyboardButton('❌ Крестики-нолики ⭕️')
btnNotebook = KeyboardButton('📘 Телефонный справочник')


genMenu = ReplyKeyboardMarkup(resize_keyboard=True) 
genMenu.add(btnCalc, btnKonfeta).add(btnKN).add(btnNotebook)
