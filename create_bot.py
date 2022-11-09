from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

open_weather_token = "5ad7b8fca6310aff7d3bdd2d7d6a2631"