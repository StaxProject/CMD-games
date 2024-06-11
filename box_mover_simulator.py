import random
import os
import msvcrt

class BoxMover:
    def __init__(self):
        self.reset()

    def reset(self):
        self.width = random.randint(30, 40)  # Увеличиваем размеры игрового поля
        self.height = random.randint(20, 30)
        self.num_boxes = random.randint(6, 10)  # Увеличиваем количество коробок
        self.generate_level()
        self.place_player_and_boxes()
        self.update_level()

    def generate_level(self):
        self.level = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.width):
            self.level[0][i] = '‖'
            self.level[self.height - 1][i] = '‖'
        for i in range(self.height):
            self.level[i][0] = '‖'
            self.level[i][self.width - 1] = '‖'
        
        num_rooms = random.randint(4, 8)  # Увеличиваем количество генерируемых комнат
        self.rooms = []
        for _ in range(num_rooms):
            self.add_room()
        self.connect_rooms()

    def add_room(self):
        room_width = random.randint(5, 10)
        room_height = random.randint(5, 10)
        start_x = random.randint(1, self.width - room_width - 2)
        start_y = random.randint(1, self.height - room_height - 2)

        room = {'x1': start_x, 'y1': start_y, 'x2': start_x + room_width, 'y2': start_y + room_height}

        self.rooms.append(room)

        for y in range(room['y1'], room['y2']):
            for x in range(room['x1'], room['x2']):
                if y == room['y1'] or y == room['y2'] - 1:
                    self.level[y][x] = '‖'
                elif x == room['x1'] or x == room['x2'] - 1:
                    self.level[y][x] = '‖'
                else:
                    self.level[y][x] = ' '

        # Create an entrance to the room
        entrance_x = random.randint(room['x1'] + 1, room['x2'] - 2)
        entrance_y = random.randint(room['y1'] + 1, room['y2'] - 2)
        self.level[entrance_y][room['x1']] = ' '
        self.level[entrance_y][room['x2'] - 1] = ' '
        self.level[room['y1']][entrance_x] = ' '
        self.level[room['y2'] - 1][entrance_x] = ' '

    def connect_rooms(self):
        for i in range(len(self.rooms) - 1):
            current_room = self.rooms[i]
            next_room = self.rooms[i + 1]

            cx, cy = (current_room['x1'] + current_room['x2']) // 2, (current_room['y1'] + current_room['y2']) // 2
            nx, ny = (next_room['x1'] + next_room['x2']) // 2, (next_room['y1'] + next_room['y2']) // 2

            while cx != nx or cy != ny:
                if cx != nx:
                    cx += 1 if cx < nx else -1
                elif cy != ny:
                    cy += 1 if cy < ny else -1
                if self.level[cy][cx] == ' ':
                    self.level[cy][cx] = ' '

    def place_player_and_boxes(self):
        self.player = [random.randint(1, self.height - 2), random.randint(1, self.width - 2)]
        while self.level[self.player[0]][self.player[1]] != ' ':
            self.player = [random.randint(1, self.height - 2), random.randint(1, self.width - 2)]
        
        self.boxes = []
        while len(self.boxes) < self.num_boxes:
            box = [random.randint(1, self.height - 2), random.randint(1, self.width - 2)]
            if box != self.player and box not in self.boxes and self.level[box[0]][box[1]] == ' ':
                self.boxes.append(box)

    def update_level(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.level[y][x] not in ['‖']:
                    self.level[y][x] = ' '
        self.level[self.player[0]][self.player[1]] = '*'
        for box in self.boxes:
            self.level[box[0]][box[1]] = '#'

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.level:
            print(' '.join(row))
        print("\nИспользуйте стрелки для перемещения.")

    def move(self, dx, dy):
        new_player = [self.player[0] + dy, self.player[1] + dx]
        if self.level[new_player[0]][new_player[1]] not in ['‖']:
            if new_player in self.boxes:
                new_box = [new_player[0] + dy, new_player[1] + dx]
                if self.level[new_box[0]][new_box[1]] not in ['‖'] and new_box not in self.boxes:
                    self.boxes[self.boxes.index(new_player)] = new_box
                    self.player = new_player
            else:
                self.player = new_player
            self.update_level()
    
    def handle_input(self, char):
        if char in [b'w', b'W']:
            self.move(0, -1)
        elif char in [b's', b'S']:
            self.move(0, 1)
        elif char in [b'a', b'A']:
            self.move(-1, 0)
        elif char in [b'd', b'D']:
            self.move(1, 0)
        elif char == b'K':  # Left arrow
            self.move(-1, 0)
        elif char == b'M':  # Right arrow
            self.move(1, 0)
        elif char == b'H':  # Up arrow
            self.move(0, -1)
        elif char == b'P':  # Down arrow
            self.move(0, 1)
        elif char in [b'r', b'R']:
            self.reset()
        elif char in [b'e', b'E']:
            self.reset()

    def check_win(self):
        # Проверка на победу: все коробки должны быть собраны в одной линии (горизонтальной или вертикальной)
        rows = {box[0] for box in self.boxes}
        cols = {box[1] for box in self.boxes}
        if len(rows) == 1 or len(cols) == 1:
            return True
        return False

def main():
    game = BoxMover()
    game.display()

def main():
    while True:
        game = BoxMover()
        game.display()

        while True:
            char = msvcrt.getch()
            if char == b'\xe0':  # Special key prefix
                char = msvcrt.getch()
            game.handle_input(char)
            game.display()
            if game.check_win():
                print("Поздравляю! Вы выиграли!")
                print("Нажмите 'q' чтобы выйти.")
                char = msvcrt.getch()
                if char == b'q' or char == b'Q':
                    return
                else:
                    break

if __name__ == "__main__":
    main()
