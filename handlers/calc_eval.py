from aiogram import types, Dispatcher
import re
from keyboards import kb_calc_eval_end, genMenu, calc_evalMenu
from data_base import db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create_bot import bot


class FCMcalc_eval(StatesGroup):
    input_value = State()
    operation = State()


async def start_calc_eval(message: types.Message) -> None:
    await FCMcalc_eval.input_value.set()
    await message.answer(text=f'Это {message.text}')
    await message.answer(text='Введите пример для решения: ', reply_markup=calc_evalMenu)

async def back_calc_eval(message: types.Message, state: FCMcalc_eval):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.answer(text=f'Вы отменили калькулятор',
                         reply_markup=genMenu)

async def operation_calc_eval(message: types.Message, state: FSMContext):
    exp = message.text.replace('/calc', '')
    exp = message.text.replace(',', '.')
    exp = message.text.replace('\\', '/')
    exp = "".join(exp.split())
    if re.match('^([-+]?([(]?[0-9][)]?[+-/*]?))*$', exp):
        try:
            await message.reply(f'Результат: {eval(exp)}', reply_markup=kb_calc_eval_end)
            await state.finish()
        except:
            await message.reply('Ошибка в рассчете, обратитесь к разработчику!')
            await db.write_to_log_calc(f'Поиск: {message.text}. Результат: ошибка в рассчете', reply_markup=kb_calc_eval_end)
            await state.finish()
    else:
        await message.reply('Ошибка ввода!')
        await db.write_to_log_calc(f'Поиск: {message.text}. Результат: ошибка ввода', reply_markup=kb_calc_eval_end)
        await state.finish()


# Кнопка Посчитать еще
async def reload_game(message: types.Message):
    await start_calc_eval(message)


# Кнопка 🔙 Выход
async def text_back_calc(message: types.Message):
    await bot.send_message(message.from_user.id, 'Попробуйте другие первоклассные проекты!', reply_markup=genMenu)


def register_handlers_calc_eval(dp: Dispatcher):
    dp.register_message_handler(start_calc_eval, text=['Улучшенный'], state=None)
    dp.register_message_handler(back_calc_eval, state="*", commands='Отмена +')
    dp.register_message_handler(back_calc_eval, Text(equals='Отмена +', ignore_case=True), state="*")
    dp.register_message_handler(operation_calc_eval, state=FCMcalc_eval.input_value)
    dp.register_message_handler(reload_game, text=['Посчитать еще +'])
    dp.register_message_handler(text_back_calc, text=['🔙 Выход 🧮+'])
