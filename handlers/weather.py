import requests
import datetime
from create_bot import open_weather_token
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class WeatherStates(StatesGroup):
    city = State()

async def weather_command(message: types.Message):
    print(f'Игрок {message.from_user.full_name} смотрит погоду!')
    await message.answer('Напиши мне название города и я пришлю сводку погоды!')
    await WeatherStates.city.set()

async def get_weather(message: types.Message, state: FSMContext):
    city = message.text
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"""<pre>***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***</pre>

Погода в городе: <b>{city}</b>
Температура: <b>{cur_weather}C°</b> <u>{wd}</u>
Влажность: <b>{humidity}%</b>
Давление: <b>{pressure} мм.рт.ст</b>
Ветер: <b>{wind} м/с</b>
Восход солнца: <b>{sunrise_timestamp}</b>
Закат солнца: <b>{sunset_timestamp}</b>
Продолжительность дня: <b>{length_of_the_day}</b>

<pre>***Хорошего дня!***</pre>""")

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")
    await state.finish()

def register_handlers_weather(dp: Dispatcher):
    dp.register_message_handler(weather_command, commands=['weather'], state=None)
    dp.register_message_handler(get_weather, state=WeatherStates.city)
