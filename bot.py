# import telebot
#
# token = "1096966689:AAFAgPzZWeV3dP6oFdVzgr3KO3Oe1D_Gr9k"
#
# bot = telebot.TeleBot(token)
#
# bot.send_message(379306493, "успех")
#
# upd = bot.get_updates()
# print(upd)
#
# import telebot
#
# token = "1096966689:AAFAgPzZWeV3dP6oFdVzgr3KO3Oe1D_Gr9k"
#
# bot = telebot.TeleBot(token)
#
# print(bot.get_me())
#
# def log(message,answer):
#     print("/n ------")
#     from datetime import datetime
#     print(datetime.now())
#     print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
#
#
# @bot.message_handler(commands=['help'])
# def handle_text(message):
#     answer = "Мои возможности ограничены. Sorry!"
#     log(message, answer)
#     bot.send_message(message.chat.id, answer )
#
# @bot.message_handler(commands=['start'])
# def handle_text(message):
#     answer = "Hello! You are welcome!"
#     log(message, answer)
#     bot.send_message(message.chat.id, answer)
#
# @bot.message_handler(commands=['settings'])
# def handle_text(message):
#     answer = "Тут пусто)"
#     log(message, answer)
#     bot.send_message(message.chat.id,answer )
#
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     answer = "Ты поц, гыгы"
#     if message.text == "a":
#         answer = "АУЕ"
#         log(message, answer)
#         bot.send_message(message.chat.id, answer)
#     elif message.text == "e":
#         answer = "Ты лол"
#         log(message, answer)
#         bot.send_message(message.chat.id,answer)
#     else:
#         log(message, answer)
#         bot.send_message(message.chat.id, answer)
#
#
# bot.polling(none_stop=True, interval=0)


import requests
import datetime

token = "1096966689:AAFAgPzZWeV3dP6oFdVzgr3KO3Oe1D_Gr9k"

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Успех')