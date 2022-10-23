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


# Меню отмены
btnCancel1 = KeyboardButton('отмена добавления')
btnCancel2 = KeyboardButton('отмена изменения')
btnCancel3 = KeyboardButton('отмена удаления')
btnCancel4 = KeyboardButton('отмена поиска')

cancelButton1 = ReplyKeyboardMarkup(resize_keyboard=True)
cancelButton1.add(btnCancel1)

cancelButton2 = ReplyKeyboardMarkup(resize_keyboard=True)
cancelButton2.add(btnCancel2)

cancelButton3 = ReplyKeyboardMarkup(resize_keyboard=True)
cancelButton3.add(btnCancel3)

cancelButton4 = ReplyKeyboardMarkup(resize_keyboard=True)
cancelButton4.add(btnCancel4)