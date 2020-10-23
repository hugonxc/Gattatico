import pyxel
import random

from sky import load_stars
from core import init_game, draw_game

FPS = 60
dt = 1 / FPS
SCREEN_W, SCREEN_H = 64*4, 64*3

def update():
    space.step(dt)

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    draw_game(space)



# Init game steps
load_stars()
space = init_game()
pyxel.init(SCREEN_W, SCREEN_H, fps=FPS)

# Load assets
pyxel.load("./assets/gattatico.pyxres")

pyxel.run(update, draw)
