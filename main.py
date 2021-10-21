from telethon import TelegramClient, events
import pytz

local_tz = pytz.timezone('Europe/Moscow')

# Вставляем api_id и api_hash
api_id = 7962471
api_hash = 'f57efb53440a511548826e0dc213eeb7'

# Тут любая строка
client = TelegramClient('b438e8e5-1705-4143-985a-b50455cb2313', api_id, api_hash)

# Тут id групп откуда получать сообщения для перенаправления
list_of_groups = [-1001541101085, -1001387647574, -1001532982961, -1001452885790, -1001371883644, 1908406198,
                  -1001428567201, -1001369492415]

# Тут идентификатор нашей группы
target_group_id = -1001127746514


@client.on(events.NewMessage(chats=list_of_groups))
async def handler(event):
    user_mess = event.message

    chat_from = event.chat if event.chat else (await event.get_chat())  # telegram MAY not send the chat enity

    #message_date = user_mess.date.replace(tzinfo=pytz.utc).astimezone(local_tz)
    #text_from = message_date.strftime("%Y.%m.%d %H:%M:%S")
    #if event.message.text != '':
    #    event.message.text = text_from + "\n" + "-" * 20 + "\n\n" + event.message.text + "\n\n" + "-" * 20 + "\n"
    #else:
    #    event.message.text = text_from + "\n"
    await client.send_message(target_group_id, user_mess)

    msg = event.message.to_dict()['message']
    if '#SHORT' in msg:
        await client.send_message(-1001582404043, event.message)
    if '#LONG' in msg:
        await client.send_message(-1001582404043, event.message)
    if 'leverage' in msg:
        await client.send_message(-1001582404043, event.message)
    if '#БЛАГОвипка' in msg:
        await client.send_message(-1001577143851, msg)
    if '#АзиатскиеКиты' in msg:
        await client.send_message(-1001543704823, event.message)
    if '#TheBull' in msg:
        await client.send_message(-1001471567039, event.message)
    if 'KeepSignalsVIP' in msg:
        await client.send_message(-1001553726038, event.message)
    if '#MarginWhales' in msg:
        await client.send_message(-1001442970105, event.message)
    if '#Dw_trade' in msg:
        await client.send_message(-1001546159152, event.message)
    if '#CryptoAngel' in msg:
        await client.send_message(-1001378134101, event.message)
    if '#Pursuit4Million' in msg:
        await client.send_message(-1001573399587, event.message)
    if '#InCryptoAnalytics' in msg:
        await client.send_message(-1001571321875, event.message)


@client.on(events.MessageEdited(chats=list_of_groups))
async def handlern(event):
    # Log the date of new edits
    user_mess = event.message

    chat_from = event.chat if event.chat else (await event.get_chat())  # telegram MAY not send the chat enity

    message_date = user_mess.date.replace(tzinfo=pytz.utc).astimezone(local_tz)
    text_from = 'CHANGED: '
    #if event.message.text != '':
    #    event.message.text = text_from + "\n" + "-" * 20 + "\n\n" + event.message.text + "\n\n" + "-" * 20 + "\n"
    #else:
    #    event.message.text = text_from + "\n"
    await client.send_message(target_group_id, user_mess)


client.start()

client.run_until_disconnected()