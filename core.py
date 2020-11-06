import pyxel
import random
from pymunk import Space, Body, Circle

from sky import draw_stars
from models import Cat, Floor, Pickle, Star

SCREEN_W, SCREEN_H = 64*4, 64*3

# Special collision methods
def dead(space, arbiter, data):
    pyxel.game_over = True
    return False

def boost(space, arbiter, data):
    for body in arbiter.bodies:
        for shape in body.shapes:
            if isinstance(shape, Pickle) or isinstance(shape, Star):
                body.velocity = (-600, 0)
                shape.collision_type = 6

    return False

def same_elem_collision(space, arbiter, data):
    return False

def zero_gravity(body, gravity, damping, dt):
    Body.update_velocity(body, (0,0), damping, dt)

# Generate elements

def generate_cat(space):
    cat = Body(mass=1, moment=1)
    cat_shape = Cat(cat, 10)
    cat_shape.elasticity = 1
    cat.position = (50, 120)
    cat_shape.collision_type = 1

    # Setup the collision callback function Cat and Pickle under boost
    g = space.add_collision_handler(1, 6)
    g.begin = same_elem_collision

    space.add(cat, cat_shape)


def generate_pickles(space):
    for i in range(0,10):
        pickle = Body(mass=1, moment=1)
        pickle_shape = Pickle(pickle, 5)
        pickle_shape.elasticity = 1

        x = random.randrange(260, 800)
        y = random.randrange(0, 180)
        pickle.position = (x, y)
        pickle.velocity_func = zero_gravity

        v = random.randrange(-20, -10)
        pickle.velocity = (v, 0)

        # Set collison type for pickle
        pickle_shape.collision_type = 2

        # Setup the collision callback function Cat and Pickle
        h = space.add_collision_handler(1, 2)
        h.begin = dead

        # Setup the collision callback function Pickle and Pickle
        p = space.add_collision_handler(2, 2)
        p.begin = same_elem_collision

        # Setup the collision callback function Pickle and Pickle under boost
        pb = space.add_collision_handler(2, 6)
        pb.begin = same_elem_collision


        space.add(pickle, pickle_shape)

def generate_stars(space):
    for i in range(0,5):
        star = Body(mass=0.00000001, moment=1)
        star_shape = Star(star, 5)

        x = random.randrange(400, 1600)
        y = random.randrange(0, 180)
        star.position = (x, y)
        star.velocity_func = zero_gravity

        v = random.randrange(-90, -50)
        star.velocity = (v, 0)
        star_shape.collision_type = 3

        # Setup the collision callback function Cat and Star
        g = space.add_collision_handler(1, 3)
        g.begin = boost

        # Setup the collision callback function Star and Star
        s = space.add_collision_handler(3, 3)
        s.begin = same_elem_collision

        # Setup the collision callback function Star and Pickle
        s = space.add_collision_handler(2, 3)
        s.begin = same_elem_collision

        # Setup the collision callback function Star and Pickle under boost
        pb = space.add_collision_handler(3, 6)
        pb.begin = same_elem_collision


        space.add(star, star_shape)

def init_game():
    sp = Space()
    # sp.gravity = (0,90)
    # sp.damping = 0.8

    # Add Cat to Space
    generate_cat(sp)

    # Add pickle to Space
    generate_pickles(sp)

    # Add star to Space
    generate_stars(sp)

    # Add floor to Space
    floor = Body(body_type=Body.STATIC)
    floor_shape = Floor(floor, (0, SCREEN_H-1), (SCREEN_W, SCREEN_H-1), 1)
    floor_shape.elasticity = 0.7
    sp.add(floor, floor_shape)

    return sp


def update_pickles(pickle, p_shape):
    if pickle.position[0] < -15:
        x = random.randrange(260, 800)
        y = random.randrange(0, 180)
        pickle.position = (x, y)

        v = random.randrange(-20, -10)
        pickle.velocity = (v, 0)

        p_shape.collision_type = 2


def update_stars(star, shape):
    if star.position[0] < -15:
        x = random.randrange(400, 1600)
        y = random.randrange(0, 180)
        star.position = (x, y)

        v = random.randrange(-90, -50)
        star.velocity = (v, 0)

        shape.collision_type = 3



def draw_game(space):
    draw_stars()
    for body in space.bodies:
        for shape in body.shapes:
            if isinstance(shape, Pickle):
                update_pickles(body, shape)

            elif isinstance(shape, Star):
                update_stars(body, shape)

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


def restart(space):
    #  Apply force based on the arrow key
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.game_over = False
        space = init_game()        

    return space
