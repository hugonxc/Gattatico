import pyxel
import random
import math

from sky import load_stars
from core import init_game, draw_game, controls, restart

FPS = 60
dt = 1 / FPS
SCREEN_W, SCREEN_H = 64*4, 64*3
points = 1
str_points = ""

def update():
    controls(space)
    space.step(dt)


def draw():
    global space
    global points
    global str_points

    if pyxel.game_over:
        pyxel.cls(pyxel.COLOR_RED)
        pyxel.text(110,80, "YOU DIED", pyxel.COLOR_WHITE)
        pyxel.text(100,100, "You scored "+str_points, pyxel.COLOR_WHITE)
        pyxel.text(80, 120, "PRESS <SPACE> TO TRY AGAIN", pyxel.COLOR_WHITE)
        space = restart(space)

    else:
        pyxel.cls(pyxel.COLOR_BLACK)
        draw_game(space)
        points = dt+points
        str_points = str(int(points))
        pyxel.text(190,10, "POINTS "+str_points, pyxel.COLOR_WHITE)


# Init game steps
load_stars()
space = init_game()
pyxel.init(SCREEN_W, SCREEN_H, fps=FPS)

# Load assets
pyxel.load("./assets/gattatico.pyxres")
pyxel.play(0, [0, 1], loop=True)

pyxel.game_over = False
pyxel.run(update, draw)
