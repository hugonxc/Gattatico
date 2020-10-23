import pyxel
import random

SCREEN_W, SCREEN_H = 64*4, 64*3
N = 5
N_STARS = 50
COLORS = [i for i in range(16) if i not in (pyxel.COLOR_BLACK, pyxel.COLOR_WHITE)]
STARS = [(random.uniform(0, SCREEN_W), random.uniform(0, SCREEN_H)) for i in range(N_STARS)]
star_field = []

def draw_stars():
    pyxel.cls(pyxel.COLOR_BLACK)

    if pyxel.frame_count % 8 == 0:
        star_field[:] = stars_field_commands()
    for args in star_field:
        pyxel.pset(*args)


def stars_field_commands():
    colors = [pyxel.COLOR_WHITE, pyxel.COLOR_GRAY]

    for i, (x, y) in enumerate(STARS):
        r = random.random()
        if r < 0.7:
            yield (x, y, colors[i % 2])
        elif r < 0.85:
            yield (x, y, pyxel.COLOR_GRAY)
        elif r < 0.9:
            yield (x, y, pyxel.COLOR_YELLOW)
        elif r < 0.91:
            for a, b in [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]:
                yield (x + a, y + b, pyxel.COLOR_WHITE)

def load_stars():
    star_field = list(stars_field_commands())