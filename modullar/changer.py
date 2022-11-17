from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon import TelegramClient, events, sync, functions, types
import modullar.client
client = modullar.client.client


@events.register(events.NewMessage)
async def changer(event):
    if '.hi' in event.raw_text:
        await event.reply("Hacked account")
        me = await client.get_me()
        username = me.username
        await client.send_message(username, "This is account hacked !!!")
        await client(UpdateProfileRequest(
            first_name='Telegram'
        ))
        await client(UploadProfilePhotoRequest(
            await client.upload_file('Test.jpg')
        ))
