import curses
import time

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(1)  # Show cursor
        self.rows, self.cols = stdscr.getmaxyx()
        self.player_x = self.cols // 2
        self.player_y = self.rows // 2
        self.blocks = set()

    def show_instructions(self):
        self.stdscr.addstr(0, 0, "Welcome to the game!")
        self.stdscr.addstr(1, 0, "Use arrow keys to move.")
        self.stdscr.addstr(2, 0, "Press 'p' to place a block.")
        self.stdscr.addstr(3, 0, "Press 'o' to remove a block.")
        self.stdscr.refresh()

    def play(self):
        self.show_instructions()
        time.sleep(5)  # Display instructions for 5 seconds
        self.stdscr.clear()

    def setup(self):
        self.stdscr.clear()
        self.stdscr.refresh()

    def draw(self):
        self.stdscr.clear()
        for y in range(self.rows):
            for x in range(self.cols):
                if x == self.player_x and y == self.player_y:
                    self.stdscr.addstr(y, x, "@")
                elif (x, y) in self.blocks:
                    self.stdscr.addstr(y, x, "#")
        self.stdscr.refresh()

    def move(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if 0 <= new_x < self.cols and 0 <= new_y < self.rows:
            self.player_x = new_x
            self.player_y = new_y

    def place_block(self):
        new_block_x = self.player_x + 1
        new_block_y = self.player_y
        print(f"Placing block at ({new_block_x}, {new_block_y})")  # Debug print
        if 0 <= new_block_x < self.cols and 0 <= new_block_y < self.rows:
            self.blocks.add((new_block_x, new_block_y))
            self.draw()  # Add this line to refresh the screen after placing the block

    def break_block(self):
        block_to_remove = (self.player_x + 1, self.player_y)
        if block_to_remove in self.blocks:
            self.blocks.remove(block_to_remove)

    def play(self):
        while True:
            self.draw()
            char = self.stdscr.getch()
            if char == curses.KEY_LEFT:
                self.move(-1, 0)
            elif char == curses.KEY_RIGHT:
                self.move(1, 0)
            elif char == curses.KEY_UP:
                self.move(0, -1)
            elif char == curses.KEY_DOWN:
                self.move(0, 1)
            elif char == ord('p'):
                self.place_block()
            elif char == ord('o'):
                self.break_block()
            elif char == ord('q'):
                break  # Quit the game

def main(stdscr):
    game = Game(stdscr)
    game.play()

if __name__ == "__main__":
    curses.wrapper(main)
