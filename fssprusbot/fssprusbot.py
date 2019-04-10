import sqlite3
from datetime import datetime
from telebot import TeleBot
from source.config import TOKEN
from source.variables import *
from fssp_api import *

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_results(message):
    while True:
        db = sqlite3.connect("fssp_api_bot.db")
        db.row_factory = dict_factory
        cursor = db.cursor()
        cursor.execute("SELECT * FROM queue WHERE state=0 and chat_id=?", (message.chat.id,))
        rows = cursor.fetchall()
        #print(rows)
        for row in rows:
            state = get_status(row['task_id'])
            #print('state ' + str(state) + ' ' + row['task_id'])
            if state == 0:
                cursor.execute("UPDATE queue SET state = 1 WHERE state=0 and chat_id=? and task_id=?",
                               (message.chat.id, row['task_id'],))
        db.close()
        return rows

def run_bot():
    bot = TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def function_name(message):
        bot.send_message(message.chat.id, start_mess)

    @bot.message_handler(commands=['help'])
    def function_name(message):
        bot.send_message(message.chat.id, help_mess)

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
            ans = get_results(message)
            for a in ans:
                msg = get_result(a['task_id'])
                print(type(msg))
                bot.send_message(message.chat.id, msg)


    bot.polling(none_stop=True, timeout=60)


if __name__ == "__main__":
    run_bot()
