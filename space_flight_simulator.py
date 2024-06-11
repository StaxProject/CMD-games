import random
import time
import keyboard
import os

# Определение размера экрана
ROWS = 30  # Увеличим количество строк
COLS = 100  # Увеличим количество столбцов

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = [
            "                                    /  \\",
            "                                 /       \\",
            "                               /           \\",
            "                               |     /\\    |",
            "                               |   /    \\  |",
            "                               |  | (  ) |  |",
            "                               |  | (  ) |  |",
            "                          /\\   |  |      |  |   /\\",
            "                         /  \\  |  |      |  |  /  \\",
            "                              | |  |      |  | |",
            "                              | | /|   .  |\\ | |",
            "                         |    | /  |   .  |  \\ |    |",
            "                         |    /    |   .  |    \\    |",
            "                         |  /      |   .  |      \\  |",
            "                         |/        |   .  |        \\|",
            "                        /         |   .  |           \\",
            "                        (          |      |           )",
            "                         |    | |--|      |--| |    |",
            "                        \\ \\//     \\ \\// \\//     \\ \\//",
            "                         \\/        \\/  \\/        \\/"
        ]

    def move_up(self):
        self.y -= 2  # Увеличиваем скорость корабля

    def move_down(self):
        self.y += 2  # Увеличиваем скорость корабля

    def move_left(self):
        self.x -= 2  # Увеличиваем скорость корабля

    def move_right(self):
        self.x += 2  # Увеличиваем скорость корабля

    def draw(self):
        for i, line in enumerate(self.symbol):
            print("\033[%s;%sH%s" % (self.y + i, self.x, line), end="", flush=True)

    def clear(self):
        for i, line in enumerate(self.symbol):
            print("\033[%s;%sH%s" % (self.y + i, self.x, " " * len(line)), end="", flush=True)

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = [
            "      *      ",
            "     ***     ",
            "    *****    ",
            "   *******   ",
            "  *********  ",
            " *********** ",
            "*************",
            " *********** ",
            "  *********  ",
            "   *******   ",
            "    *****    ",
            "     ***     ",
            "      *      "
        ]

    def move_down(self):
        self.y += 1

    def draw(self):
        for i, line in enumerate(self.symbol):
            print("\033[%s;%sH%s" % (self.y + i, self.x, line), end="", flush=True)

    def clear(self):
        for i, line in enumerate(self.symbol):
            print("\033[%s;%sH%s" % (self.y + i, self.x, " " * len(line)), end="", flush=True)

def main():
    os.system('cls')
    print("Welcome to Space Flight Simulator!")
    print("Use arrow keys to move. Avoid * and collect +")
    print("Press Q to quit.")
    time.sleep(2)
    
    spaceship = Spaceship(COLS//2, ROWS//2)
    asteroids = []
    score = 0

    while True:
        os.system('cls')
        spaceship.draw()

        for asteroid in asteroids:
            asteroid.move_down()
            asteroid.draw()

            if asteroid.y >= ROWS:
                asteroids.remove(asteroid)
                score += 1

            if asteroid.x == spaceship.x and asteroid.y == spaceship.y:
                print("\033[%s;%sH%s" % (ROWS//2, COLS//2-5, "Game Over!"))
                print("\033[%s;%sH%s" % (ROWS//2+1, COLS//2-7, "Your score: %d" % score))
                score = 0  # Сброс счета
                time.sleep(2)  # Пауза перед продолжением игры
                spaceship.x = COLS // 2
                spaceship.y = ROWS // 2
                asteroids.clear
                continue  # Продолжаем игру без выхода

        if keyboard.is_pressed('q'):
            print("\033[%s;%sH%s" % (ROWS//2, COLS//2-5, "Quitting..."))
            return
        elif keyboard.is_pressed('up'):
            spaceship.move_up()
        elif keyboard.is_pressed('down'):
            spaceship.move_down()
        elif keyboard.is_pressed('right'):
            spaceship.move_right()
        elif keyboard.is_pressed('left'):
            spaceship.move_left()

        if random.random() < 0.01:  # Уменьшаем скорость появления метеоритов
            asteroids.append(Asteroid(random.randint(1, COLS), 1))

        time.sleep(0.05)  # Управление скоростью анимации

if __name__ == "__main__":
    main()
