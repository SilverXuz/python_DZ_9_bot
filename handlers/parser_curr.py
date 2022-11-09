import requests                               #pip install requests
# from bs4 import BeautifulSoup                #pip install beautifulsoup4
import datetime
from aiogram import types
from aiogram.dispatcher import Dispatcher
import pandas as pd                           #pip install pandas
import matplotlib.pyplot as plt               #pip install matplotlib
from create_bot import bot
from aiogram.types import InputFile


async def curr_rate_command(message: types.Message):
    print(f'Игрок {message.from_user.full_name} смотрит курс валют!')
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    s = requests.get(url)
    data = s.json()
    # print(data)

    USD = data["Valute"]["USD"]["Value"]
    USD_name = data["Valute"]["USD"]["Name"]
    EUR = data["Valute"]["EUR"]["Value"]
    EUR_name = data["Valute"]["EUR"]["Name"]
    CNY = data["Valute"]["CNY"]["Value"]
    CNY_name = data["Valute"]["CNY"]["Name"]

    await message.reply(f"""<pre>***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***</pre>

<pre>Курсы валют по отношению к Российскому рублю.</pre>

<u>USD💵  {USD_name}:</u>  <b>{USD}</b>
<u>EUR💶  {EUR_name}:</u>  <b>{EUR}</b>
<u>CNY💴  {CNY_name}:</u>  <b>{CNY}</b>

""")

    marks = pd.Series({
    "USD": USD,
    "EUR": EUR,
    "CNY": CNY,
    })

    
    plt.bar(marks.index[0], color="r", height=marks[0], label="USD")
    plt.bar(marks.index[1], color="g", height=marks[1], label="EUR")
    plt.bar(marks.index[2], color="y", height=marks[2], label="CNY")

    plt.legend()
    plt.savefig("curr_rate.png")
    # plt.show()
    
    photo = InputFile("curr_rate.png")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    
""" Это копия того в каком виде хранятся данные в джейсоне!!!
"USD": {
    "ID": "R01235",
    "NumCode": "840",
    "CharCode": "USD",
    "Nominal": 1,
    "Name": "Доллар США",
    "Value": 61.0611,
    "Previous": 60.9774

"EUR": {
    "ID": "R01239",
    "NumCode": "978",
    "CharCode": "EUR",
    "Nominal": 1,
    "Name": "Евро",
    "Value": 61.2445,
    "Previous": 60.8231

"CNY": {
    "ID": "R01375",
    "NumCode": "156",
    "CharCode": "CNY",
    "Nominal": 10,
    "Name": "Китайских юаней",
    "Value": 83.9724,
    "Previous": 83.6997
"""

def register_handlers_parser_curr(dp: Dispatcher):
    dp.register_message_handler(curr_rate_command, commands=['curr_rate'])
