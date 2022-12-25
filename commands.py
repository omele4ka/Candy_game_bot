from bot_config import dp, bot
from aiogram import types
import controller
import random

total = 150
max_step = 28

@dp.message_handler(commands='start')
async def starting(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Давай сыграем в конфетки? '
                                                 f'Напиши /yes, если согласен')


@dp.message_handler(commands='yes')
async def confirm(message: types.Message):
    global total
    if controller.whoes_first() == True:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, твой ход! '
                                                     f'На столе 150 конфет. Можно взять от 1 до 28. Сколько ты возьмешь?')
    else:
        await bot.send_message(message.from_user.id, f'Пeрвым ходит бот')
        bot_step = random.randint(1, max_step)
        total -= bot_step
        await bot.send_message(message.from_user.id, f'Бот взял {bot_step} конфет, на столе осталось {total}')
        return total

@dp.message_handler()
async def all_bot(message: types.Message):
    global total
    if total <= 0:
        await message.reply(f'{message.from_user.first_name}, все конфеты закончились. Сыграем еще раз? Пиши /start')
    else:
        player_step = int(message.text)
        if player_step < 1 or player_step > 28 or player_step > total:
            await bot.send_message(message.from_user.id,
                                   f'Ах ты хитрый жук, {message.from_user.first_name}, не жульничай!')
        else:
            total -= player_step
            if total == 0:
                await bot.send_message(message.from_user.id, f'Ура! Ты победил(а)!')
            else:
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                             f'ты взял(а) {message.text} конфет и на столе осталось {total}')
                bot_step = 0
                if total < 29:
                    bot_step = total
                else:
                    bot_step = random.randint(1, 28)
                total -= bot_step
                if total == 0:
                    await bot.send_message(message.from_user.id, f'Сорри, Бот победил')
                else:
                    await bot.send_message(message.from_user.id,
                                           f'Бот взял {bot_step} конфет, на столе осталось {total}')




