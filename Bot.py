import telebot

mybot = telebot.TeleBot('880698305:AAGp4i7-mbskWv2TGITTLF7tHnm77wawFho')


@mybot.message_handler(commands=['start'])
def start_message(message):
    mybot.send_message(message.chat.id, 'Hello')


@mybot.message_handler(commands=['finish'])
def start_message(message):
    mybot.send_message(message.chat.id, 'Bye')


mybot.polling()

