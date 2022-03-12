from telethon import TelegramClient
import time

api_id = 17351392
api_hash = '5a5d096e04df8a9d2440f752bea9e420'
username = 'clamator'


client = TelegramClient(username, api_id, api_hash)
client.send_message('me', 'Hello, myself!')

