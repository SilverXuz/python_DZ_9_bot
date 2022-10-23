import csv
# import datetime
# from aiogram.types.message import ContentType






async def write_to_file_state(state, filename='directory.csv'):
    """
    Функция которая производит запись в справочник.
    """
    async with state.proxy() as data:
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
            writer = csv.DictWriter(csvfile, fieldnames=title, delimiter=',')
            writer.writerow(data)
            print(data)


async def write_to_file(contact: dict, filename='directory.csv'):
    """
    Функция которая производит запись в справочник.
    """
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title, delimiter=',')
        writer.writerow(contact)

async def overwrite_file(data: list, filename='directory.csv'):
    """
    Функция которая  объединяет два списка после удаления. До строки удаления и после. и записывает в справочник.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title)
        for row in data:
            writer.writerow(dict(zip(title, row)))


async def get_data_from_file(filename='directory.csv') -> list:
    """
    Функция которая считывает файл
    """
    result = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)
    return result
