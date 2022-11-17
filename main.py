from telethon import TelegramClient, events, sync
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest

import modullar.client
import modullar.changer
client = modullar.client.client

with client as darknet:
    darknet.add_event_handler(modullar.changer.changer)


client.start()
client.run_until_disconnected()
