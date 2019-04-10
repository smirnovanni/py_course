from telebot import TeleBot


def run_bot():
    bot = TeleBot('626685841:AAE1zzVFHyB1cYcjipwcFT9EgQaacs_cq3E')

    @bot.message_handler(commands=['start'])
    def function_name(message):
        bot.send_message(message.chat.id, 'Ну начнёмс!')

    @bot.message_handler(content_types=['text'])
    def function_name(message):
        bot.send_message(message.chat.id, message.text)

    bot.polling(none_stop=True)


if __name__ == "__main__":
    run_bot()
