import curses

from homework03.life import GameOfLife


def __init__(self, life: GameOfLife) -> None:
    super().__init__(life)


def draw_borders(self, screen) -> None:
    """ Отобразить рамку. """
    pass


def draw_grid(self, screen) -> None:
    """ Отобразить состояние клеток. """
    pass


def run(self) -> None:
    screen = curses.initscr()
    # PUT YOUR CODE HERE
    curses.endwin()