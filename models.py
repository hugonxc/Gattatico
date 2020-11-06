from pymunk import Circle, Segment
import pyxel


class Cat(Circle):
    def draw(self):
        IMG = 0
        IMG_X, IMG_Y = 0,88
        WIDTH, HEIGHT = 47,30
        BKG = pyxel.COLOR_BLACK

        x, y = self.body.position
        pyxel.blt(x, y, IMG, IMG_X, IMG_Y, WIDTH, HEIGHT, BKG)


class Floor(Segment):
    def draw(self):
        IMG = 0
        IMG_X, IMG_Y = 5,5
        WIDTH, HEIGHT = 6,6
        BKG = pyxel.COLOR_BLACK

        ax, ay = self.body.position + self.a
        bx, by = self.body.position + self.b
        pyxel.line(ax, ay, bx, by, pyxel.COLOR_WHITE)
        # pyxel.blt(x, y, IMG, IMG_X, IMG_Y, WIDTH, HEIGHT, BKG)

    
class Pickle(Circle):
    def draw(self):
        IMG = 0
        IMG_X, IMG_Y = 0,3
        WIDTH, HEIGHT = 26, 10
        BKG = pyxel.COLOR_BLACK

        x, y = self.body.position
        pyxel.blt(x, y, IMG, IMG_X, IMG_Y, WIDTH, HEIGHT, BKG)


class Star(Circle):
    def draw(self):
        IMG = 0
        IMG_X, IMG_Y = 0,48
        WIDTH, HEIGHT = 21,20
        BKG = pyxel.COLOR_BLACK

        x, y = self.body.position
        pyxel.blt(x, y, IMG, IMG_X, IMG_Y, WIDTH, HEIGHT, BKG)