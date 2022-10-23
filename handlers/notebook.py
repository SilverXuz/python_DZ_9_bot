from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import notebookMenu, genMenu, cancelButton1, cancelButton2, cancelButton3, cancelButton4
from data_base import db
from aiogram.dispatcher.filters import Text


"""**************************************     ДОБАВЛЕНИЕ КОНТАКТА     ******************************************"""
class FSMAddContact(StatesGroup):
    surname = State()
    name = State()
    personal_number = State()
    work_number = State()
    city = State()
    comment = State()



async def commands_addContact(message: types.Message) -> None:
    await FSMAddContact.surname.set()
    await message.reply('Введите фамилию: ', reply_markup=cancelButton1)

async def cancel_add(message: types.Message, state: FSMAddContact):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.reply('Вы прервали добавление контакта!', reply_markup=notebookMenu)

async def add_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
        print('Фамилия записана: ', message.from_user.id, message.text)
    await FSMAddContact.next()
    await message.reply('Введите имя: ', reply_markup=cancelButton1)

async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print('Имя записано: ', message.from_user.id, message.text)
    await FSMAddContact.next()
    await message.reply('Введите личный телефон: ', reply_markup=cancelButton1)

async def add_personal_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['personal_number'] = message.text
        print('Личный телефон записан: ', message.from_user.id, message.text)
    await FSMAddContact.next()
    await message.reply('Введите рабочий телефон: ', reply_markup=cancelButton1)

async def add_work_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_number'] = message.text
        print('Рабочий телефон записан: ', message.from_user.id, message.text)
    await FSMAddContact.next()
    await message.reply('Введите город: ', reply_markup=cancelButton1)

async def add_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        print('Город записан: ', message.from_user.id, message.text)
    await FSMAddContact.next()
    await message.reply('Введите примечание: ', reply_markup=cancelButton1)

async def add_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
        print('Комментарий записан: ', message.from_user.id, message.text)
    await db.write_to_file_state(state)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Контакт удачно сохранен в справочник!', reply_markup=notebookMenu)



"""**************************************     ИЗМЕНЕНИЕ КОНТАКТА     ******************************************"""
class FSMeditContact(StatesGroup):
    find_contact = State()
    input_edit_id = State()
    validation_id = State()



async def commands_edit_contact(message: types.Message) -> None:
    await FSMeditContact.find_contact.set()
    await message.reply('Введите данные контакта, который хотите изменить, и посмотрите его ID: ', reply_markup=cancelButton2)   

async def cancel_edit(message: types.Message, state: FSMAddContact):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.reply('Вы прервали измненеие контакта!', reply_markup=notebookMenu)

async def edit_find_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['find_contact'] = message.text
        print('Информация для поиска: ', message.text)
        contact_indexes = await search(message.text)
        if len(contact_indexes) <= 0:            
            await message.answer('Контакт не найден', reply_markup=notebookMenu)
            await db.write_to_log(f'Поиск: {message.text}. Результат: контакт не найден')
        else:
            output = await print_contacts_by_index(contact_indexes)
            await message.answer(output)
    await FSMeditContact.next()
    await message.reply('Введите ID который нужно изменить: ', reply_markup=cancelButton2)

async def edit_input_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['input_edit_id'] = message.text
        print('ID для измнения записан: ', message.text)
    await delete_contact(message.text)
    await state.finish()
    await message.answer('Введите новые данные по контакту: ', reply_markup=cancelButton2)
    await commands_addContact(message)


async def delete_contact(del_id: str):
    """
    Функция будет вносить измнения в контакт по индексу. Через удаление и перезапись.
    """
    del_id = int(del_id)
    data = await db.get_data_from_file()
    data.pop(del_id)
    await db.overwrite_file(data)


"""**************************************     УДАЛЕНИЕ КОНТАКТА     ******************************************"""
class FSMdelContact(StatesGroup):
    find_contact = State()
    input_del_id = State()
    

async def commands_del_contact(message: types.Message) -> None:
    await FSMdelContact.find_contact.set()
    await message.reply('Введите данные контакта, который хотите удалить, и посмотрите его ID: ', reply_markup=cancelButton3)   

async def cancel_del(message: types.Message, state: FSMAddContact):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.reply('Вы прервали удаление контакта!', reply_markup=notebookMenu)
    
async def del_find_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['find_contact'] = message.text
        print('Информация для поиска: ', message.text)
        contact_indexes = await search(message.text)
        if len(contact_indexes) <= 0:            
            await message.answer('Контакт не найден', reply_markup=notebookMenu)
            await db.write_to_log(f'Поиск: {message.text}. Результат: контакт не найден')
        else:
            output = await print_contacts_by_index(contact_indexes)
            await message.answer(output)
    await FSMdelContact.next()
    await message.reply('Введите ID который нужно удалить: ', reply_markup=cancelButton3)

async def delete_input_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['input_del_id'] = message.text
        print('ID для удаления записан: ', message.text)
    await delete_contact(message.text)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Контакт удален из справочника! *(индексы обновлены)*', reply_markup=notebookMenu)


async def delete_contact(del_id: str):
    """
    Функция будет удалять найденный контакт по индексу
    """
    del_id = int(del_id)
    data = await db.get_data_from_file()
    data.pop(del_id)
    await db.overwrite_file(data)


"""**************************************     НАЙТИ КОНТАКТ     ******************************************"""
class FSMfindContact(StatesGroup):
    find_contact = State()
    

async def commands_find_contact(message: types.Message) -> None:
    await FSMfindContact.find_contact.set()
    await message.reply('Введите данные контакта, который хотите найти: ', reply_markup=cancelButton4)   

async def cancel_find(message: types.Message, state: FSMAddContact):
    curent_state = await state.get_state()
    if curent_state is None:
        return
    await state.finish()
    await message.reply('Вы прервали поиск контакта!', reply_markup=notebookMenu)
    
async def search_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['find_contact'] = message.text
        print('Информация для поиска: ', message.text)
        contact_indexes = await search(message.text)
        if len(contact_indexes) <= 0:            
            await message.answer('Контакт не найден', reply_markup=notebookMenu)
            await db.write_to_log(f'Поиск: {message.text}. Результат: контакт не найден')
        else:
            output = await print_contacts_by_index(contact_indexes)
            await message.answer(output)
            await bot.send_message(message.from_user.id, 'Выведены все найденные совпадения!', reply_markup=notebookMenu)
    await state.finish()



"""**************************************     ВЫВЕСТИ ВЕСЬ СПИСОК     ***************************************"""
async def all_notebook(message: types.Message):
    data = await db.get_data_from_file()
    output = await print_all_contacts(data)
    await message.answer(output)    

async def print_all_contacts(data: list):
    """
    Функция будет выводить все найденные контакты. На вход принимает содержимое всего файла *.csv
    """
    # print('ID', 'ФАМИЛИЯ', 'ИМЯ', 'ЛИЧНЫЙ ТЕЛЕФОН', 'РАБОЧИЙ ТЕЛЕФОН', 'ГОРОД', 'ПРИМЕЧАНИЕ', sep='\t\t')
    d = {}
    for i, row in enumerate(data):            
        d[i] = row
    result = (f'ID, фамилия, имя, телефон, личный, телефон, рабочий, город, примечание\n\
    {d}')
    return result


"""**************************************     ОБЩИЕ ФУНКЦИИ     ******************************************"""

async def search(message: types.Message):
    """
    Функция возвращает список индексов строк, в которых найдена строка value.
    """
    result = []
    data = await db.get_data_from_file()
    for i, row in enumerate(data):
        for col in row:
            if message.lower() in col.lower():
                result.append(i)
    return result


async def print_contacts_by_index(message: types.Message):
    """
    Функция будет выводить все строки по индексу с найденными совпадениями поиска
    """
    data = await db.get_data_from_file()
    d = {}
    for i, row in enumerate(data):    
        if i in message:          
            d[i] = row
    result = (f'ID, фамилия, имя, телефон, личный, телефон, рабочий, город, примечание\n\
    {d}')
    return result


# Команда 📘 Телефонный справочник
async def main(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=notebookMenu)


# Кнопка 🔙 Выход
async def text_back(message : types.Message):
    await bot.send_message(message.from_user.id, 'Попробуйте другие первоклассные проекты!', reply_markup=genMenu)


def register_handlers_notebook(dp : Dispatcher):
    dp.register_message_handler(main, text=['📘 Телефонный справочник'])
    dp.register_message_handler(text_back, text=['🔙 Выход'])
    

    dp.register_message_handler(commands_addContact, text=['Добавить контакт'], state=None)
    dp.register_message_handler(cancel_add, state="*", commands='отмена добавления')
    dp.register_message_handler(cancel_add, Text(equals='отмена добавления', ignore_case=True), state="*")
    dp.register_message_handler(add_surname, state=FSMAddContact.surname)
    dp.register_message_handler(add_name, state=FSMAddContact.name)
    dp.register_message_handler(add_personal_number, state=FSMAddContact.personal_number)
    dp.register_message_handler(add_work_number, state=FSMAddContact.work_number)
    dp.register_message_handler(add_city, state=FSMAddContact.city)
    dp.register_message_handler(add_comment, state=FSMAddContact.comment)

    dp.register_message_handler(commands_edit_contact, text=['Изменить контакт'], state=None)
    dp.register_message_handler(cancel_edit, state="*", commands='отмена изменения')
    dp.register_message_handler(cancel_edit, Text(equals='отмена изменения', ignore_case=True), state="*")
    dp.register_message_handler(edit_find_contact, state=FSMeditContact.find_contact)
    dp.register_message_handler(edit_input_id, state=FSMeditContact.input_edit_id)

    dp.register_message_handler(commands_del_contact, text=['Удалить контакт'], state=None)
    dp.register_message_handler(cancel_del, state="*", commands='отмена удаления')
    dp.register_message_handler(cancel_del, Text(equals='отмена удаления', ignore_case=True), state="*")
    dp.register_message_handler(del_find_contact, state=FSMdelContact.find_contact)
    dp.register_message_handler(delete_input_id, state=FSMdelContact.input_del_id)

    dp.register_message_handler(commands_find_contact, text=['Найти контакт'], state=None)
    dp.register_message_handler(cancel_find, state="*", commands='отмена поиска')
    dp.register_message_handler(cancel_find, Text(equals='отмена поиска', ignore_case=True), state="*")
    dp.register_message_handler(search_contact, state=FSMfindContact.find_contact)

    dp.register_message_handler(all_notebook, text=['Посмотреть весь справочник'])
