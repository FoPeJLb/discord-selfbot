import inquirer
import sys
import os
import random
import requests
import time
import json
import platform
import re
import shutil
from colorama import init, Back, Style

#Обозначение файла с данными о пользователе
filename = "data.txt"


# Функция возврата в главное меню
def back_to_menu():
    pass

# Функция записи данных пользователя
def user_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_info = {} # словарь для хранения информации
    fields = ["Auth. Key", "Chat ID", "Username", "User ID"]
    for field in fields:
        value = input("Введите значение для {}: ".format(field))
        user_info[field] = value
        print("Сохраненная информация:")
    for saved_field, saved_value in user_info.items():
        print(saved_field + ": " + saved_value)
        print("-" * 15)
    # Сохранение информации в текстовый файл
    with open("data.txt", "w") as file:
        for field, value in user_info.items():
            file.write(f"{field}: {value}\n")
    print("Информация сохранена в файл data.txt")
    back_to_menu()

# Провека наличия файла
if not os.path.exists(filename):
    # Если файла нет, вызываем функцию
    os.system('cls' if os.name == 'nt' else 'clear')
    user_info()
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    pass

# Функция поиска слова в определённой позиции текстового файла
def find_word_in_specific_position(filename, position):
    with open(filename, 'r') as file:
        text = file.read().split()
        file.close()
    if position < len(text):
        word = text[position]
        return f"{word}"

# Блок с позициями нужных для авторизации данных в текстовом файле
f_authkey = 2
f_chatid = 5
f_username = 7
f_userid = 10

# Данные о пользователе
authkey = find_word_in_specific_position(filename, f_authkey)
chatid = find_word_in_specific_position(filename, f_chatid)
usr = find_word_in_specific_position(filename, f_username)
usrid = find_word_in_specific_position(filename, f_userid)

# Функция, отвечающая за закрашивание экрана определённым цветом
def screen_color():
     # Инициализация модуля colorama
        init()
        # Определение цвета фона и стиля текста
        background_color = Back.WHITE
        text_style = Style.BRIGHT
        # Получение размеров терминала
        columns, rows = shutil.get_terminal_size()
        # Очистка экрана
        print('\033[2J')
        # Засветка экрана
        for _ in range(rows):
            print(f'{background_color}{text_style} ' * columns)
            time.sleep(0.0003) # Приостановка выполнения программы на 0.0003 секунду
        # Сброс цвета фона и стиля текста в исходное состояние
        print('\033[0m')
        # Очистка экрана
        print('\033[2J')

# Функция, отвечающая за вспышку на экране со звуковым сопровождением
def flash_screen():
    opsys = platform.system()
    if opsys == "Windows":
        screen_color()
        # Воспроизведение звукового сигнала (Зависит от ОС)
        print('\a')
    elif opsys == "Linux":
        screen_color()
        os.system(["paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"])
    elif opsys == "Darwin":
        screen_color()
        os.system(["afplay", "/System/Library/Sounds/Glass.aiff"])
    else:
        pass

# Функция удаления сообщения
def deletemsg():
    auth = {'authorization': f'{authkey}'}
    d = requests.get(f"https://discord.com/api/v9/channels/{chatid}/messages", headers=auth)
    username = ['{usr}']
    userid = ['{usrid}']
    jsonn = json.loads(d.text)
    item = jsonn[0]
    delmsg = requests.delete(f"https://discord.com/api/v9/channels/{chatid}/messages/{item['id']}", headers=auth)

# Функция изменения сообщения
def modmsg():
    auth = {'authorization': f'{authkey}'}
    m = requests.get(f"https://discord.com/api/v9/channels/{chatid}/messages", headers=auth)
    jsonn = json.loads(m.text)
    item = jsonn[0]
    txt = ['ㅤ']
    payload = {'content': txt}
    h = requests.patch(f"https://discord.com/api/v9/channels/{chatid}/messages/{item['id']}", data=payload, headers=auth)

## Функции, которые относятся к кубику:

# Функция анимации кубика
def cubeanim():
    os.system('cls' if os.name == 'nt' else 'clear')
    auth = {'authorization': f'{authkey}'}
    m = requests.get(f"https://discord.com/api/v9/channels/{chatid}/messages", headers=auth)
    jsonn = json.loads(m.text)
    item = jsonn[0]
    lst = ['1 ⚀', '2 ⚁', '3 ⚂', '4 ⚃', '5 ⚄', '6 ⚅']
    qube = random.choice(lst)
    txt = [f'{qube}']
    print(f'{qube}')
    payload = {'content': txt}
    p = requests.patch(f"https://discord.com/api/v9/channels/{chatid}/messages/{item['id']}", data=payload, headers=auth)

# Функция завершения анимации кубика
def fincube():
    os.system('cls' if os.name == 'nt' else 'clear')
    auth = {'authorization': f'{authkey}'}
    m = requests.get(f"https://discord.com/api/v9/channels/{chatid}/messages", headers=auth)
    jsonn = json.loads(m.text)
    item = jsonn[0]
    lst = ['1 ⚀', '2 ⚁', '3 ⚂', '4 ⚃', '5 ⚄', '6 ⚅']
    qube = random.choice(lst)
    txt = [f'Кубик выпал на:\n{qube}']
    print(f'Кубик выпал на:\n{qube}')
    payload = {'content': txt}
    p = requests.patch(f"https://discord.com/api/v9/channels/{chatid}/messages/{item['id']}", data=payload, headers=auth)

# Кубик
def cube():
    os.system('cls' if os.name == 'nt' else 'clear')
    lst = ['1 ⚀', '2 ⚁', '3 ⚂', '4 ⚃', '5 ⚄', '6 ⚅']
    qube = random.choice(lst)
    txt = [f'{qube}']
    payload = {'content': txt}
    header = {'authorization': f'{authkey}'}
    r = requests.post(f"https://discord.com/api/v9/channels/{chatid}/messages", data=payload, headers=header)
    flash_screen()
    cubeanim()
    cubeanim()
    time.sleep(0.05)
    cubeanim()
    time.sleep(0.10)
    cubeanim()
    time.sleep(0.15)
    cubeanim()
    time.sleep(0.20)
    cubeanim()
    modmsg()
    cubeanim()
    modmsg()
    cubeanim()
    modmsg()
    flash_screen()
    fincube()
    time.sleep(5)
    deletemsg()
    flash_screen()

# Функция выхода из приложения
def exit():
    sys.exit
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция замены одного слова на другое в текстовом файле
def replace_word():
    # Чтение содержимого файла
    os.system('cls' if os.name == 'nt' else 'clear')
    old_word = f'{chatid}'
    with open(filename, 'r') as file:
        content = file.read()
        file.close()
    # Запрос нового слова у пользователя
    new_word = input("Введите новый Chat ID: ")
    # Замена слова с использованием регулярного выражения
    new_content = re.sub(r'\b{}\b'.format(old_word), new_word, content)
    # Запись нового содержимого в файл
    with open(filename, 'w') as file:
        file.write(new_content)
        file.close()
    print("Информация сохранена в файл data.txt")
    back_to_menu()

# Создание меню
os.system('cls' if os.name == 'nt' else 'clear')
menu = [
    inquirer.List('choice',
    message="Выберите действие:",
    choices=[
        ('Бросить кубик', cube),
        ('Изменить данные', user_info),
        ('Изменить Chat ID', replace_word),
        ('Выход', exit),
        ],
    ),
]

### Конец программы

#Цикл для работы меню
while True:
    answers = inquirer.prompt(menu)
    selected_action = answers["choice"]

    if selected_action == back_to_menu: # проверяем выбранное действие
        continue # переходим обратно в начало цикла
    elif selected_action == exit: # проверяем выбранное действие
        os.system('cls' if os.name == 'nt' else 'clear')
        break # выходим из цикла
    else:
        selected_action()
        print("Нажмите Enter, чтобы вернуться в меню.")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
