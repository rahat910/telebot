import telebot
from time import sleep

TOKEN =  "7090483880:AAHHAC1Srr6lmVulCanuXIN9ojmtQkjECos"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text=="кандайсын":
        bot.send_message(message.from_user.id,"алхамдулилла")
    elif message.text=="иштер кандай":
        sleep(5)
        bot.send_message(message.from_user.id, "Нормально")

    elif message.text=="мне клп":
        sleep(2)
        bot.send_message(message.from_user.id, "Нормально")    

    else:
        bot.send_message(message.from_user.id, "Мен сени тушунбодум") 


bot.infinity_polling()           

