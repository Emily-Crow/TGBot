print("Пакет 'run' подключен!")

from BotConnect import bot
    
@bot.message_handler(commands=['run'])
def start_message(message):
    ##print("4.2")
    bot.send_message(message.chat.id,"Запущено")
    exec(open("./Modules/start.py").read())
