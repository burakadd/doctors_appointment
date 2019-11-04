import telebot

bot = telebot.TeleBot('880698305:AAGp4i7-mbskWv2TGITTLF7tHnm77wawFho')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Привет, ты написал мне /start',
        reply_markup=keyboard1
    )


# @mybot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         mybot.send_message(message.from_user.id,
#                          "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         mybot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         mybot.send_message(message.from_user.id,
#                          "Я тебя не понимаю. Напиши /help.")


# @mybot.message_handler(content_types=['sticker'])
# def get_sticker(message):
#     print(message)
#
# @mybot.message_handler(commands=['start'])
# def start_message(message):
#     mybot.send_message(message.chat.id, 'Привет')
#
# @mybot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text:
#         mybot.send_message(message.from_user.id, "!!")
#         mybot.send_sticker(message.chat.id, 'CAADAQADLgMAAj1jrQdLwWiQYSl9kRYE')
    # elif message.text == "/help":
    #     mybot.send_message(message.from_user.id, "Напиши привет")
    # else:
    #     mybot.send_message(message.from_user.id,
    #                      "Я тебя не понимаю. Напиши /help.")



# @mybot.message_handler(commands=['start'])
# def start_message(message):
#     mybot.send_message(message.chat.id, 'Hello')
#
#
# @mybot.message_handler(commands=['finish'])
# def start_message(message):
#     mybot.send_message(message.chat.id, 'Bye')


bot.polling()

