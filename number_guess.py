import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def guess_number():
    while True:
        # Генерируем случайное число от 1 до 100
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print_slow("Добро пожаловать в игру 'Угадай число'!")
        print_slow("Сегодняшним ведущим будет...")

        # Выбираем случайного ведущего
        host = random.choice(["Шмидтти", "Джон", "Томас", "Ричард", "Мэйсон", "Логан", "Оливер", "Лукас", "Бенджамин", "Картер"])
        print_slow(f"{host}!")

        print_slow(f"Он загадал число от 1 до 100. Попробуйте угадать, {host} будет давать вам подсказки!")

        while True:
            guess = input("Введи свою догадку: ")

            # Проверяем, введено ли корректное число
            if not guess.isdigit():
                print_slow("Пожалуйста, введите число.")
                continue

            guess = int(guess)
            attempts += 1

            # Проверяем, угадал ли игрок число
            if guess < secret_number:
                print_slow("Мое число больше.")
            elif guess > secret_number:
                print_slow("Мое число меньше.")
            else:
                print_slow(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break

        play_again = input("Хочешь сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            print_slow("Спасибо за игру! До новых встреч!")
            break

if __name__ == "__main__":
    guess_number()
