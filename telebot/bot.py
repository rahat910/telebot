import telebot


TOKEN = '7090483880:AAHHAC1Srr6lmVulCanuXIN9ojmtQkjECos'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет! Я бот.")

    # Отправка изображения
    with open('777714_Bloomberg-News_ISLAMIC-MOSQUE_trans_NvBQzQNjv4BqIQEVKj27zX9KV9Q7rAZYf-Nd1VaroVtfDVIngsAV4lM.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="Добро пожаловать в магазин ADYLSHOP")




@bot.message_handler(commands=['nike'])
def send_welcome(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет! Я бот.")

    # Отправка изображения
    with open('photo_2024-07-03_15-04-25.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="Добро пожаловать в магазин ADYLSHOP")
       

@bot.message_handler(commands=['video'])
def send_welcome(message):
            # Отправка приветственного сообщения
            bot.reply_to(message, "Привет! вот тебе рекламные видеоролик")

            # Отправка видео
            with open('Новая_Красивейшая_Заставка_Исламские_Видеоролики_.mp4', 'rb') as vid:
                bot.send_video(message.chat.id, vid, caption="Это видео.")

@bot.message_handler(commands=['help'])
def send_help(message):
    # Отправка сообщения со справкой
    bot.reply_to(message, "Это справочное сообщение. Введите /start для начала работы с ботом.")

@bot.message_handler(commands=['audio'])
def send_welcome(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет! Я бот с аудиосообщением.")

    # Отправка аудиосообщения
    with open('audio_2024-07-05_09-53-26.ogg', 'rb') as audio:
        bot.send_voice(message.chat.id, audio)



# Обработчик для кнопок
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton('Кнопка 1')
    button2 = telebot.types.KeyboardButton('Кнопка 2')
    keyboard.add(button1, button2)

    # Отправка сообщения с клавиатурой
    bot.reply_to(message, "Выберите кнопку:", reply_markup=keyboard)

# Запуск бота
bot.polling()

