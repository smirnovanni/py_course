from telebot import TeleBot
import fssp_api

def run_bot():
    bot = TeleBot('719958666:AAEmt0CT6CJS_xZvChdSXlb3RnipzzYK214')

    @bot.message_handler(commands=['start'])
    def function_name(message):
        bot.send_message(message.chat.id, 'Введите ФИО!')

    @bot.message_handler(content_types=['text'])
    def function_name(message):
        bot.send_message(message.chat.id, message.text)

    bot.polling(none_stop=True)


if __name__ == "__main__":
    run_bot()
