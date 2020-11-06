import pyxel
import random

from sky import load_stars
from core import init_game, draw_game, controls, restart

FPS = 60
dt = 1 / FPS
SCREEN_W, SCREEN_H = 64*4, 64*3

def update():
    controls(space)
    space.step(dt)


def draw():
    global space

    if pyxel.game_over:
        pyxel.cls(pyxel.COLOR_RED)
        pyxel.text(110,80, "YOU DIED", pyxel.COLOR_WHITE)
        pyxel.text(80, 100, "PRESS <SPACE> TO TRY AGAIN", pyxel.COLOR_WHITE)
        space = restart(space)

    else:
        pyxel.cls(pyxel.COLOR_BLACK)
        draw_game(space)

# Init game steps
load_stars()
space = init_game()
pyxel.init(SCREEN_W, SCREEN_H, fps=FPS)

# Load assets
pyxel.load("./assets/gattatico.pyxres")

pyxel.game_over = False
pyxel.run(update, draw)
