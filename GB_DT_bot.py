from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('Бот GB_DreamTeam_Project_bot успешно запущен!')


from handlers import calc_eval, calc, calc_eval, client, konfeta, krest_null, notebook, other

calc_eval.register_handlers_calc_eval(dp)
calc.register_handlers_calc(dp)
client.register_handlers_client(dp)  
konfeta.register_handlers_konfeta(dp)
krest_null.register_handlers_krest_null(dp)
notebook.register_handlers_notebook(dp)
# other.register_handlers_other(dp) # Этот хендлер должен быть всегда последним!!!




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
