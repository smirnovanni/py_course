import sqlite3
from datetime import datetime

from telebot import TeleBot

from fssp_api import *


def run_bot():
    bot = TeleBot('719958666:AAEmt0CT6CJS_xZvChdSXlb3RnipzzYK214')

    @bot.message_handler(commands=['start'])
    def function_name(message):
        bot.send_message(message.chat.id, 'Введите ФИО!')

    @bot.message_handler(content_types=['text'])
    def function_name(message):
        db = sqlite3.connect("fssp_api_bot.db")
        region, firstname, lastname, secondname, birthdate = str(message.text).split(' ')
        task_id = send_req(region=region, firstname=firstname, lastname=lastname, secondname=secondname,
                           birthdate=birthdate)
        try:
            cursor = db.cursor()
            cursor.execute("""INSERT INTO queue({columns}) VALUES (?, ?, ?, ?)
            """.format(columns='task_id, date, state, chat_id'),
                           (task_id, datetime.now().strftime('%d.%m.%Y'), 0, message.chat.id))
            db.commit()
            db.close()
        except:
            bot.send_message(message.chat.id, "Попробуйте позже")
        finally:
            bot.register_next_step_handler(message, get_results)

    def get_results(message):
        while True:
            db = sqlite3.connect("fssp_api_bot.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM queue WHERE state=0 and chat_id=?", (message.chat.id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                state = get_status(row[1])
                if state == 0:
                    msg = get_result(row[1])
                    print(msg)
                    bot.send_message(message.chat.id, msg)
                    cursor.execute("UPDATE queue SET state = 1 WHERE state=0 and chat_id=? and task_id=?",
                                   (message.chat.id, row[1],))

            db.close()

    bot.polling(none_stop=True, timeout=120)


if __name__ == "__main__":
    run_bot()
