from tokenj import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
import logging
import sql

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

DB=sql.SQLite('myDB.db')
index=0

@dp.message_handler(commands = ['start'])
async def l(message:types.Message):
        button = types.KeyboardButton("добавить запись")
        button1 = types.KeyboardButton ( "Просмотреть записи" )
        button2 = types.KeyboardButton ( "удалить запись по номеру" )
        button3 = types.KeyboardButton ( "последняя добавленая" )
        button4 = types.KeyboardButton ( "Авто удаление" )
        board=types.ReplyKeyboardMarkup(resize_keyboard = True).add(button1, button2, button3, button4, button)
        await message.answer('hello', reply_markup = board)


@dp.message_handler()#
async def inline(message: types.Message):

    if inline.index==1:
        DB.add_list(message.from_user.id, message.text)
        if len(DB.get_list ( message.from_user.id ))>inline.max:
            DB.delete_list ( 1 , message.from_user.id )
        await message.reply ( 'сообщение добавлено' )
        inline.index=0
    elif inline.index==3:
        try:
            DB.delete_list( int(message.text),message.from_user.id)
            await message.reply('сообщение удалено')
            inline.index = 0
        except:
            await message.reply('Надо вводить число\n Повторите попытку')
    elif inline.index==5:
        try:
            inline.max=int(message.text)
            i=len(DB.get_list ( message.from_user.id ))-inline.max
            while i:
                i-=1
                DB.delete_list ( 0 , message.from_user.id )
            await message.reply('Ok')
            inline.index=0
        except:
            await message.reply('Надо вводить число\n Повторите попытку')
        

    if message.text=="добавить запись":
        await message.answer ( 'напишите заметку' )
        inline.index = 1
    elif message.text == "удалить запись по номеру":
        m = DB.get_list ( message.from_user.id )
        i=1
        for mm in m:
            await message.answer ( str(i)+')'+mm[2] )
            i+=1
        await message.answer ( 'напишите номер' )
        inline.index = 3
    elif message.text == "Просмотреть записи":
        m = DB.get_list ( message.from_user.id )
        for mm in m:
            await message.answer ( mm[2] )
    elif message.text == "последняя добавленая":
        c=DB.get_list(message.from_user.id)
        await message.reply(c[-1][2])
    elif message.text == "Авто удаление":
        inline.index = 5
        await message.answer('Сколь вы хотите одновременно хранить записей')


inline.index=0
inline.max=100

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)