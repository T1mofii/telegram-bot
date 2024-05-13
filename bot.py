import telebot

bot = telebot.TeleBot('7124726550:AAG1fyj4esn9uACTiaLz1C0X5BZnCUFykpM')

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

bot.polling(non_stop=True)
