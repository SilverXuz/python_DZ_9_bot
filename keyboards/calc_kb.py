from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


"""*******************************************  Калькулятор ********************************************"""
btnSumm = KeyboardButton('+')
btnDiff = KeyboardButton('-')
btnMult = KeyboardButton('*')
btnDiv = KeyboardButton('/')
btnCancel_calc = KeyboardButton('Отмена')
btnReload_calc = KeyboardButton('Посчитать еще')
btnBack_calc = KeyboardButton('🔙 Выход 🧮')
btnChangesCalc = KeyboardButton('Простой')
btnChangesCalcEval = KeyboardButton('Улучшенный')

calcMenu = ReplyKeyboardMarkup(resize_keyboard=True)
calcMenu.row(btnSumm, btnDiff, btnMult, btnDiv).add(btnCancel_calc)

kb_calc_end = ReplyKeyboardMarkup(resize_keyboard=True)
kb_calc_end.add(btnBack_calc, btnReload_calc)

changesMenu = ReplyKeyboardMarkup(resize_keyboard=True)
changesMenu.add(btnChangesCalc, btnChangesCalcEval)


"""*******************************************  Калькулятор + ********************************************"""
btnReload_calc_eval = KeyboardButton('Посчитать еще +')
btnBack_calc_eval = KeyboardButton('🔙 Выход 🧮+')
btnCancel_calc_eval = KeyboardButton('Отмена +')

calc_evalMenu = ReplyKeyboardMarkup(resize_keyboard=True)
calc_evalMenu.add(btnCancel_calc_eval)

kb_calc_eval_end = ReplyKeyboardMarkup(resize_keyboard=True)
kb_calc_eval_end.add(btnBack_calc_eval, btnReload_calc_eval)
