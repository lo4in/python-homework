import telebot
from telebot import types

# Создаём бота
API_TOKEN = '7292516254:AAFL-v3Ke3v1ORVW1piIvAWk571RO5dX6bU'
bot = telebot.TeleBot(API_TOKEN)

# Данные для авторизации учителя
ADMIN_LOGIN = "zarnigor"
ADMIN_PASSWORD = "123456789"

# Обработчики команд
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Я учитель", "Я ученик")
    bot.send_message(message.chat.id, "Выберите, кто вы:", reply_markup=markup)

# Для учителей
@bot.message_handler(func=lambda m: m.text == "Я учитель")
def teacher_login(message):
    bot.send_message(message.chat.id, "Введите логин и пароль через пробел (пример: admin admin):")
    bot.register_next_step_handler(message, check_teacher_login)

def check_teacher_login(message):
    try:
        login, password = message.text.split()
        if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
            bot.send_message(message.chat.id, "Авторизация успешна. Введите название файла для ответов теста:")
            bot.register_next_step_handler(message, create_test_file)
        else:
            bot.send_message(message.chat.id, "Неверный логин или пароль.")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка формата. Введите логин и пароль через пробел.")

def create_test_file(message):
    global test_file_name
    test_file_name = message.text
    with open(test_file_name, "w") as file:
        pass  # Создаём пустой файл
    bot.send_message(message.chat.id, f"Файл '{test_file_name}' создан. Введите список правильных ответов через пробел:")
    bot.register_next_step_handler(message, save_test_keys)

def save_test_keys(message):
    key_list = message.text.upper()
    key_list = key_list.split()
    record = ' '.join(key_list)
    with open(test_file_name, "a") as file:
        file.write(f'{record}\n')
    bot.send_message(message.chat.id, "Ответы сохранены.")

# Для учеников
@bot.message_handler(func=lambda m: m.text == "Я ученик")
def student_name(message):
    bot.send_message(message.chat.id, "Введите ваше имя:")
    bot.register_next_step_handler(message, ask_test_name)

def ask_test_name(message):
    student_name = message.text
    bot.send_message(message.chat.id, "Введите название теста, который хотите проверить:")
    bot.register_next_step_handler(message, check_test_answers, student_name)

def check_test_answers(message, student_name):
    try:
        test_name = message.text
        with open(test_name, "r") as file:
            key_list = file.read().split()
        bot.send_message(message.chat.id, "Введите ваши ответы через пробел:")
        bot.register_next_step_handler(message, evaluate_answers, key_list)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл с таким названием не найден.")

def evaluate_answers(message, key_list):
    stud_answ_list = message.text.upper().split()
    correct_ans = [item for item in stud_answ_list if item in key_list]
    incorrect_ans = [item for item in stud_answ_list if item not in key_list]

    response = (f"Ваши правильные ответы: {correct_ans}\n"
                f"Ваши неправильные ответы: {incorrect_ans}\n"
                f"Количество правильных ответов: {len(correct_ans)}\n"
                f"Количество неправильных ответов: {len(incorrect_ans)}")

    bot.send_message(message.chat.id, response)

# Запуск бота
bot.polling(none_stop=True)
