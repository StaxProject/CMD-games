import random
import string
import os
import webbrowser
import time

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, number):
    filename = f'password_{number}.txt'
    with open(filename, 'w') as file:
        file.write(password)
    return filename

def read_password_from_file(filename):
    with open(filename, 'r') as file:
        password = file.read().strip()
    return password

def delete_password_files(num_files):
    for i in range(1, num_files + 1):
        filename = f'password_{i}.txt'
        if os.path.exists(filename):
            os.remove(filename)
            print_with_delay(f'Файл {filename} удален.')

def unusual_action():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Ссылка на "Rick Astley - Never Gonna Give You Up"
    webbrowser.open(url)
    print_with_delay("Поздравляю! Ты ввел все пароли. Вот небольшой сюрприз для тебя!")

def print_with_delay(text, delay=0.05, end=''):
    for char in text:
        print(char, end=end, flush=True)
        time.sleep(delay)
    print()


def final_dialog(num_passwords):
    dialog = [
        "Это было не то, чтобы сложно...",
        "Но и легким это задание тоже назвать нельзя...",
        "Всё слишком однотипно и утомительно, не так ли?",
        """Тут и спрашивать смысла нет. Каждый ответит "Да!" """,
        "Хочешь узнать, ради чего ты всё это делал?",
        "Уверен?",
        "Я бы не был так уверен и решителен на твоем месте...",
        "Ты скачал и запустил абсолютно неизвестную программу...",
        "Тут может быть абсолютно всё, что угодно.",
        "Но не мне решать твой выбор.",
        "Ты хочешь посмотреть что там?"
    ]

    for line in dialog:
        input(print_with_delay(line))
    
    choice = input("1.Да\n2.Нет конечно\nВыбор: ")
    
    if choice == '1':
        unusual_action()
    else:
        print_with_delay("Вот и правильно!")

    delete_password_files(num_passwords)
    input("Для выхода нажмите ENTER...")
    

def show_rules():
    names = [
        "Шмидтти", "Джон", "Томас", "Ричард", "Мэйсон", 
        "Логан", "Оливер", "Лукас", "Бенджамин", "Картер"
    ]
    name = random.choice(names)
    rules = (
        f"Привет! Меня зовут {name} и я ваш ведущий сегодня.\n"
        "Правила игры просты:\n"
        "1. Я буду генерировать пароли и сохранять их в файлы.\n"
        "2. Вам нужно будет открыть файл, прочитать пароль и ввести его в программу.\n"
        "3. Всего будет 10 паролей.\n"
        "4. Если вы введете все пароли правильно, вас ждет небольшой сюрприз!\n"
        "Готовы начать? Тогда приступим!\n"
    )
    print_with_delay(rules)

def main():
    show_rules()
    num_passwords = 10
    correct_entries = 0

    save_phrases = [
        "Пароль сохранен в файл", "Пароль записан в файл", 
        "Пароль сохранен в документ", "Пароль записан в документ",
        "Файл с паролем сохранен", "Документ с паролем записан",
        "Пароль успешно сохранен в файл", "Пароль успешно записан в файл",
        "Пароль сохранен", "Пароль записан"
    ]
    
    correct_phrases = [
        "Пароль верный!", "Пароль правильный!", 
        "Верный пароль!", "Пароль введен верно!",
        "Правильный пароль!", "Ты ввел правильный пароль!",
        "Ты ввел верный пароль!", "Пароль подтвержден!",
        "Пароль совпадает!", "Пароль принят!"
    ]
    
    incorrect_phrases = [
        "Пароль неверный. Попробуйте еще раз.", "Пароль неправильный. Попробуйте снова.", 
        "Неверный пароль. Введите еще раз.", "Пароль не совпадает. Попробуйте еще раз.", 
        "Пароль неверный. Введите снова.", "Неправильный пароль. Попробуйте еще раз.",
        "Пароль неверный. Попробуйте ввести его еще раз.", "Пароль неправильный. Попробуйте еще раз.",
        "Пароль не совпадает. Введите его снова.", "Пароль неверный. Попробуйте еще разок."
    ]

    for i in range(1, num_passwords + 1):
        password = generate_password()
        filename = save_password_to_file(password, i)
        print_with_delay(f'Пароль {i} сохранен в файл {filename}. {random.choice(save_phrases)}')
        
        user_input = input(f'Введите пароль из файла {filename}: ')
        correct_password = read_password_from_file(filename)
        
        if user_input == correct_password:
            print_with_delay(random.choice(correct_phrases))
            correct_entries += 1
        else:
            print_with_delay(random.choice(incorrect_phrases))
            break

    if correct_entries == num_passwords:
        final_dialog(num_passwords)

if __name__ == "__main__":
    main()
