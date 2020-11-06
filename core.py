import pyxel
from pymunk import Space, Body, Circle

from sky import draw_stars
from models import Cat, Floor, Pickle, Star

SCREEN_W, SCREEN_H = 64*4, 64*3

def dead(space, arbiter, data):
    pyxel.game_over = True
    return True

def boost(space, arbiter, data):
    print("BOOST")
    arbiter.remove(arbiter.bodies[2])
    arbiter.bodies[1].apply_impulse_at_local_point((-30,0),(0,0))
    
    return True

def init_game():
    sp = Space()
    # sp.gravity = (0,90)
    # sp.damping = 0.8

    # Add Cat to Space
    cat = Body(mass=1, moment=1)
    cat_shape = Cat(cat, 10)
    cat_shape.elasticity = 1
    cat.position = (50, 120)
    cat_shape.collision_type = 1
    sp.add(cat, cat_shape)

    # Add pickle to Space
    pickle = Body(mass=1, moment=1)
    pickle_shape = Pickle(pickle, 5)
    pickle_shape.elasticity = 1
    pickle.position = (180, 120)
    pickle.velocity_func = zero_gravity
    pickle.velocity = (0, 0)
    pickle_shape.collision_type = 2

    # Setup the collision callback function Cat and Pickle
    h = sp.add_collision_handler(1, 2)
    h.begin = dead

    sp.add(pickle, pickle_shape)


    # Add star to Space
    star = Body(mass=0.00000001, moment=1)
    star_shape = Star(star, 5)
    star.position = (90, 120)
    star.velocity_func = zero_gravity
    star.velocity = (0, 0)
    star_shape.collision_type = 3

    # Setup the collision callback function Cat and Star
    g = sp.add_collision_handler(1, 3)
    g.begin = boost

    sp.add(star, star_shape)


    # Add floor to Space
    floor = Body(body_type=Body.STATIC)
    floor_shape = Floor(floor, (0, SCREEN_H-1), (SCREEN_W, SCREEN_H-1), 1)
    floor_shape.elasticity = 0.7
    sp.add(floor, floor_shape)


    return sp


def draw_game(space):
    draw_stars()
    for body in space.bodies:
        for shape in body.shapes:
            shape.draw()


def controls(space):
    #  Apply force based on the arrow key
    if pyxel.btn(pyxel.KEY_UP):
        space.bodies[0].apply_force_at_local_point((0, -300), (0,0))

    elif pyxel.btn(pyxel.KEY_DOWN):
        space.bodies[0].apply_force_at_local_point((0, 200), (0,0))

    # elif pyxel.btnr(pyxel.KEY_LEFT):
    #     space.bodies[0].apply_force_at_local_point((-1000, 0), (0,0))

    # elif pyxel.btnr(pyxel.KEY_RIGHT):
    #     space.bodies[0].apply_force_at_local_point((1000, 0), (0,0))


def zero_gravity(body, gravity, damping, dt):
    Body.update_velocity(body, (0,0), damping, dt)
