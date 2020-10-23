from pymunk import Space, Body, Circle

from sky import draw_stars

from models import Cat, Floor

SCREEN_W, SCREEN_H = 64*4, 64*3

def init_game():
    sp = Space()
    sp.gravity = (0,50)
    sp.damping = 0.8

    # Add Cat to Space
    cat = Body(mass=1, moment=1)
    cat_shape = Cat(cat, 5)
    cat_shape.elasticity = 1
    sp.add(cat, cat_shape)

    # Add floor to Space
    floor = Body(body_type=Body.STATIC)
    floor_shape = Floor(floor, (0, SCREEN_H-1), (SCREEN_W, SCREEN_H-1), 1)
    floor_shape.elasticity = 1
    sp.add(floor, floor_shape)



    return sp


def draw_game(space):
    draw_stars()
    for body in space.bodies:
        for shape in body.shapes:
            shape.draw()