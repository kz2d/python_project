from conf import API_TOCEN, SQLite
from aiogram import Bot, Dispatcher, executor, types
import logging


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOCEN)
dp = Dispatcher(bot)

db=SQLite('data\\db.db')

@dp.message_handler(commands = 'subscribe')
async def send_welcome(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id, True)
    await message.answer(message.text)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands = 'unsubscribe')
async def send_lol(message: types.Message):
    if (not db.subscriber_exists ( message.from_user.id )):
        db.add_subscriber ( message.from_user.id, status = False )
    else:
        db.update_subscription ( message.from_user.id , False )

    await message.answer("no no")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
