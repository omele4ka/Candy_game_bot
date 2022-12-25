from aiogram.utils import executor

import handlers
from bot_config import dp
import handlers

async def bot_start(_):
    print('Бот запущен')

handlers.register_handler(dp)

if __name__ =='__main__':
    executor.start_polling(dispatcher=dp, on_startup=bot_start)

