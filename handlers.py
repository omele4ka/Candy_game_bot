from aiogram import types, Dispatcher
from bot_config import dp
import commands

def register_handler(db: Dispatcher):
    dp.register_message_handler(commands.starting, commands='start')
    dp.register_message_handler(commands.all_bot)

