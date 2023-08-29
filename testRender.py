import pygame as pg
from config import *


pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((win_width, win_height))


# coordinate offset/scaling
def c(x, y, scale=1):
    return (scale * x + win_width / 2, win_height / 2 - scale * y)


def grid(scale_x=scale, scale_y=scale, colour=GRID_COL):
    for x in range(-win_width, win_width, scale_x):
        pg.draw.line(screen, colour, c(x, -win_height), c(x, win_height))
    for y in range(-win_height, win_height, scale_y):
        pg.draw.line(screen, colour, c(-win_width, y), c(win_width, y))


pg.display.set_caption("Simple Renderer")
exit = False

while not exit:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True

    screen.fill(BKG_COL)
    grid()
    pg.draw.circle(screen, RED, c(0, 0), point_size)
    pg.draw.circle(screen, YELLOW, c(2, 4, 10), point_size)

    pg.display.update()
