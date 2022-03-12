from telethon import TelegramClient
import time
# Use your own values from my.telegram.org
api_id = 17351392
api_hash = '5a5d096e04df8a9d2440f752bea9e420'
username = 'clamator'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient(username, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

async def main():
    while True:
        await client.send_message(-1001781672815, '/Любой текст/')
        await client.send_message(-1001781672815, '/Любой текст')
        time.sleep(1)


with client:
    client.loop.run_until_complete(main())
