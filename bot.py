import os
from flask import Flask, request
import telebot

# Устанавливаем токен вашего бота
TOKEN = '7124726550:AAG1fyj4esn9uACTiaLz1C0X5BZnCUFykpM'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# Замените 'YOUR_DOMAIN' на ваше доменное имя сервера
WEBHOOK_URL = f'https://telegram-bot-rurchik-4ac0317f5b9d.herokuapp.com/{TOKEN}'

# Обработчик для вебхука
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

# Установка вебхука
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

# Обработчики команд и сообщений вашего бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Ты замерз?")
    bot.register_next_step_handler(message, check_freezing)

def check_freezing(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, "Тебя согреть?")
        bot.register_next_step_handler(message, warm_up)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, "Тогда иди нахуй баран))")
    else:
        bot.send_message(message.chat.id, "Долбоеб, ответ только да или нет")

def warm_up(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, "Насколько сильно тебя согреть? (по 100 бальной шкале)")
        bot.register_next_step_handler(message, send_stickers)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, "Тогда иди нахуй баран))")
    else:
        bot.send_message(message.chat.id, "Долбоеб, ответ только да или нет")

def send_stickers(message):
    try:
        sticker_count = int(message.text)
        sticker_id = 'CAACAgIAAxkBAVaEWWZCQkbRiS76vwUxDpZHVm2Q394mAAKdKwAC85wgS4jS1WHMKaPINQQ' 
        for _ in range(sticker_count):
            bot.send_sticker(message.chat.id, sticker_id)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")

# Запуск сервера Flask
if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
