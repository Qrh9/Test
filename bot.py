from telethon import TelegramClient, events
api_id = '24179928'
api_hash = 'e19c1340234edd892cee9c38bb68439c'
bot_token = '6899343302:AAG0XQGw2-na6-JoT26dhcbFwwKGDZAieSY'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
@bot.on(events.NewMessage(pattern='/start', incoming=True))
async def start(event):
    sender = await event.get_sender()
    sender_id = sender.id
    await event.reply('هلو')#(
    
print ("gays")

def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()