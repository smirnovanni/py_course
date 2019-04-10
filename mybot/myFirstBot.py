from telebot import TeleBot
import json

#'719958666:AAEmt0CT6CJS_xZvChdSXlb3RnipzzYK214'
#'626685841:AAE1zzVFHyB1cYcjipwcFT9EgQaacs_cq3E'
def run_bot():
    bot = TeleBot('719958666:AAEmt0CT6CJS_xZvChdSXlb3RnipzzYK214')

    @bot.message_handler(commands=['start'])
    def function_name(message):
        bot.send_message(message.chat.id, 'Ну начнёмс!', )

    @bot.message_handler(content_types=['text'])
    def function_name(message):
        bot.send_message(message.chat.id, message.text)

    @bot.message_handler(content_types=['location'])
    def handle_location(message):
        print("{0}, {1}".format(message.location.latitude, message.location.longitude))

    @bot.message_handler(content_types=['sticker'])
    def function_name(message):
        print(message)
        #print(json.dumps(message, sort_keys=True, indent=4))
        bot.send_sticker(message.from_user.id, message.sticker.file_id)

    bot.polling(none_stop=True, timeout=60)


if __name__ == "__main__":
    run_bot()
