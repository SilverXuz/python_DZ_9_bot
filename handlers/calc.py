from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import calcMenu, genMenu, kb_calc_end
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Text


class CalcStates(StatesGroup):
    waiting_for_first_number = State()
    waiting_for_operation = State()
    waiting_for_second_number = State()


async def start_calculation(message: types.Message):
    print(f'Игрок {message.from_user.full_name} пользуется Простой 🧮 Калькулятор!')
    await message.answer('Напишите первое число: ', reply_markup=calcMenu)
    await CalcStates.waiting_for_first_number.set()

async def cancel_calc(message: types.Message, state: FSMContext):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.reply('Вы отменили калькулятор!', reply_markup=genMenu)

async def choosing_first_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Некоректный ввод. Попробуйте снова.', reply_markup=calcMenu)
        return
    await state.update_data(first_number=int(message.text))
    await CalcStates.next()
    await message.answer('Выберете операцию с помощью кнопок: ', reply_markup=calcMenu)

async def choosing_operation(message: types.Message, state: FSMContext):
    AVAILABLE_OPERATIONS = ['+', '-', '*', '/']
    if message.text not in AVAILABLE_OPERATIONS:
        await message.answer('Недопустимая операция.Попробуйте снова.', reply_markup=calcMenu)
        return
    await state.update_data(operation=message.text)
    await CalcStates.next()
    await message.answer('Введите второе число: ', reply_markup=calcMenu)

async def choosing_second_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Некоректный ввод. Попробуйте снова.', reply_markup=calcMenu)
        return
    user_data = await state.get_data()
    oper = user_data['operation']
    first_number = user_data['first_number']
    second_number = int(message.text)
    result = 0
    if oper == '+':
        result = first_number+second_number
    elif oper == '-':
        result = first_number-second_number
    elif oper == '*':
        result = first_number*second_number
    elif oper == '/':
        result = first_number/second_number
    await message.answer(f'Результат {result}', reply_markup=kb_calc_end)
    await state.finish()

# Кнопка Посчитать еще
async def reload_game(message: types.Message):
    await start_calculation(message)


# Кнопка 🔙 Выход
async def text_back_calc(message: types.Message):
    await bot.send_message(message.from_user.id, 'Попробуйте другие первоклассные проекты!', reply_markup=genMenu)


def register_handlers_calc(dp: Dispatcher):
    dp.register_message_handler(start_calculation, text='Простой', state='*')
    dp.register_message_handler(cancel_calc, state="*", commands='Отмена')
    dp.register_message_handler(cancel_calc, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(choosing_first_number, state=CalcStates.waiting_for_first_number)
    dp.register_message_handler(choosing_operation, state=CalcStates.waiting_for_operation)
    dp.register_message_handler(choosing_second_number, state=CalcStates.waiting_for_second_number)
    dp.register_message_handler(reload_game, text=['Посчитать еще'])
    dp.register_message_handler(text_back_calc, text=['🔙 Выход 🧮'])
