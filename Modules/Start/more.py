print("Пакет 'more' подключен!")

from BotConnect import bot

def more():
    @bot.message_handler(commands=['more'])
    def start_message(message):
        bot.send_message(message.chat.id,"MORE")

        @bot.message_handler(commands=['one'])
        def start_message(message):
            bot.send_message(message.chat.id,"one")
            bot.send_message(message.chat.id,"More one")
