from random import random
from turtle import (
    colormode, pencolor, goto, dot, ontimer,
    setup, hideturtle, tracer, up, done
)
from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    """Wrap value around -200 and 200."""
    if value > 200:
        return -200
    if value < -200:
        return 200
    return value  # TODO


def draw():
    """Move ant and draw screen."""
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    colormode(255)
    r = int(ant.x % 255)
    g = int(ant.y % 255)
    b = 200
    pencolor(r, g, b)

    goto(ant.x, ant.y)
    dot(4)

    ontimer(draw, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
done()
