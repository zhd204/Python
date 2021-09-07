# Turtle graphics documentation https://docs.python.org/3/library/turtle.html
# Turtle colors https://cs111.wellesley.edu/labs/lab01/colors
# Turtle colors at trinket https://trinket.io/docs/colors

from turtle import Turtle, Screen
import random


def dashed_line(t, interval):
    """
    Draw a dashed line which composes a solid part and gap part.
    :param t: turtle object
    :param interval: distance for either the solid portion or gap portion, total length of the dashed line is 2 x interval
    :return: none
    """
    t.pendown()
    t.forward(interval)
    t.penup()
    t.forward(interval)
    t.pendown()


def polygon(n, l):
    """
    Draw a polygon.
    :param n: number of vertices
    :param l: length of each side (equilateral polygon)
    :return: none
    """
    for _ in range(n):
        tim.right(360 / n)
        tim.forward(l)


def random_walk(t):
    """
    :param t: turtle object
    :return: none
    """
    random_distance = random.randint(30, 30)
    random_angle = random.choice([0, 90])
    random_direction = random.choice(['forward', 'backward'])
    random_turn = random.choice(['left', 'right'])
    random_color = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
    random_speed = random.randint(1, 10)

    t.pensize(15)
    t.pencolor(random_color)
    t.speed(random_speed)
    if random_turn == 'left':
        t.left(random_angle)
    else:
        t.right(random_angle)

    if random_direction == 'forward':
        t.forward(random_distance)
    # else:
    #     t.backward(random_distance)


def random_color_rgb():
    random_color = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
    return random_color


def draw_spirograph(size_of_gap, t):
    for _ in range(int(360 / size_of_gap)):
        t.pencolor(random_color_rgb())
        t.circle(100, steps=100)
        t.setheading(t.heading() + size_of_gap)


screen = Screen()
# screen.screensize(canvwidth=1980, canvheight=1080)
tim = Turtle()
tim.shape()
tim.color('red')

# # Draw a square
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
#
# # Draw a pentagon
# for _ in range(5):
#     tim.right(360 / 5)
#     tim.forward(100)

# # Draw polygons
# screen.colormode(255)
# for i in range(3, 13):
#     color_tup = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     tim.pencolor(color_tup)
#     polygon(i, 100)

# # Random walk
# screen.colormode(255)
# for _ in range(200):
#     random_walk(tim)

# Draw a spirograph
tim.speed(10)
screen.colormode(255)
draw_spirograph(2, tim)

# # Draw a dashed line.
# for _ in range(15):
#     dashed_line(tim, 10)

screen.exitonclick()
