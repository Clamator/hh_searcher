from pyrogram import Client, filters
import tgcrypto

#app = Client('my_account1')
#txt = 'test'
#username2 = '1001781672815'
#@app.on_message(filters.me)
#def echo(client, message):
#    message.reply_text(txt)
with Client('my_account1') as app:
    app.send_message('me', 'hello')

app.run()