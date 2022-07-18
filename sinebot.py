import telebot

# 5562227020:AAHjRyhXa-jv7iEpU4KPi3GYoSeqPP1gRmE

bot = telebot.TeleBot('5562227020:AAHjRyhXa-jv7iEpU4KPi3GYoSeqPP1gRmE')


name = ''
surname = ''
age = 0


def reg_name(message):
    global name
    # в глобальную переменную name записывается имя пользователя
    name = message.text
    # Продолжаем
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    # то же самое
    surname = message.text
    # Продолжаем
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age

    # пишем бесконечный цикл до тех пор, пока пользователь не введёт возраст цифрами
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введи цифры?')
    keaboard = telebot.types.InlineKeyboardMarkup()
    # ответы да или нет пойдут в callback_data
    key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')
    keaboard.add(key_yes)
    key_no = telebot.types.InlineKeyboardButton(text='нет', callback_data='no')
    keaboard.add(key_no)
    bot.send_message(message.from_user.id, f'Тебе {age} лет, и тебя зовут {name} {surname}? ', reply_markup=keaboard)

# обработчик сообщений определяет фильтры через которые должно пройти сообщение
@bot.message_handler(commands=['start', 'help'])
# если проходит фильтр, то функция декорации вызывается
# входящее сообщение передаётся как аргумент
def send_welcome(message): # может иметь произвольное имя, но только один параметр - message
    # будет выводить это сообщение на команды /start, /help
    bot.reply_to(message, 'AAAAAAAAAA')



@bot.message_handler(func=lambda m: True)# обрабатывает любое сообщение така как True
def eeell(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Привет, создатель бота!')
    elif message.text == 'hi':
        bot.reply_to(message, 'WAZZAP!!!')
        # 1-передали id нашего чата, 2-сообщение
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет! Давай познакомимся! Как тебя завут?')
        # потом бот перепрыгивает на следующий шаг, запускается функция reg_name
        bot.register_next_step_handler(message, reg_name)

# обработчик call back
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, f'Приятно познакомимться {name}! теперь ты в БД!')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'ПДавайте попробуем заново')
        bot.send_message(call.message.chat.id, 'Привет! Давай познакомимся! Как тебя завут?')
        bot.register_next_step_handler(call.message, reg_name)



bot.polling()