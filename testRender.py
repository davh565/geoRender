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


def point(x, y, colour=POINT_COL, size=point_size, scale=scale, frame=screen):
    pg.draw.circle(frame, colour, c(x, y, scale), size)


def line(x1, y1, x2, y2, colour=LINE_COL, width=line_width, scale=scale, frame=screen):
    pg.draw.line(frame, colour, c(x1, y1, scale), c(x2, y2, scale), width)


def line2(slope, offset, colour=LINE_COL, width=line_width, scale=scale, frame=screen):
    x1 = -win_width // (2 * scale)
    y1 = slope * x1 + offset
    x2 = win_width // (2 * scale)
    y2 = slope * x2 + offset
    pg.draw.line(frame, colour, c(x1, y1, scale), c(x2, y2, scale), width)


def plane(x1, y1, x2, y2, x3, y3, colour=PLANE_COL, scale=scale, frame=screen):
    pg.draw.polygon(
        frame, colour, [c(x1, y1, scale), c(x2, y2, scale), c(x3, y3, scale)]
    )


pg.display.set_caption("Simple Renderer")
exit = False

while not exit:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True

    screen.fill(BKG_COL)
    grid()
    line(0, 0, 3.7, 2.1)
    line2(0.5, -1, RED)
    line2(0.5, 0, RED)
    point(0, 0, RED)
    point(3.7, 2.1)
    point(-1, 1, YELLOW)
    plane(0, 0, 3.7, 2.1, -1, 1, CYAN)

    pg.display.update()
