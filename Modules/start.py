print("Пакет 'start' подключен!")
from BotConnect import bot
##from Modules.Start.more import more

@bot.message_handler(commands=['start'])
def start_message(message):
    ##print("2.2")
    bot.send_message(message.chat.id,"Привет ✌️ ")
        
    @bot.message_handler(commands=['more'])
    def start_message(message):
        bot.send_message(message.chat.id,"MORE")

        @bot.message_handler(commands=['one'])
        def start_message(message):
            bot.send_message(message.chat.id,"one")
            bot.send_message(message.chat.id,"More one")

