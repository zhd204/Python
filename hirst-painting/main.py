# Colorgram package https://github.com/obskyr/colorgram.py
import turtle

import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

color_list = rgb_colors[3:]
print(color_list)

screen = t.Screen()

t.colormode(255)

pointer = t.Turtle()
pointer.penup()
print(pointer.pos())
pointer.hideturtle()
pointer.setposition(-250, -150)
pointer_normal_speed = pointer.speed()
print(pointer.pos())
for _ in range(10):
    current_row_starting_point = pointer.position()
    for _ in range(10):
        pointer.dot(20, random.choice(color_list))
        pointer.forward(50)
    pointer.speed(10)
    pointer.setposition(current_row_starting_point)
    pointer.setheading(90)
    pointer.forward(50)
    pointer.setheading(0)
    pointer.speed(pointer_normal_speed)

screen.exitonclick()
