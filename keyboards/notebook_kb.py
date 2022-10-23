from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры главного меню


btnaddContact = KeyboardButton('Добавить контакт')
btneditContact = KeyboardButton('Изменить контакт')
btndelContact = KeyboardButton('Удалить контакт')
btnoneContact = KeyboardButton('Найти контакт')
btnallContact = KeyboardButton('Посмотреть весь справочник')
btnBack = KeyboardButton('🔙 Выход')

notebookMenu = ReplyKeyboardMarkup(resize_keyboard=True) 
notebookMenu.add(btnaddContact, btnoneContact).add(btneditContact, btndelContact).add(btnallContact).add(btnBack)
