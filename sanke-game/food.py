from turtle import Turtle
import random
from snake import MOVE_DISTANCE
from math import fabs


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.95, stretch_len=0.95)
        self.penup()
        self.speed("fastest")
        self.goto(next(self.new_xcor()), next(self.new_ycor()))
        print(f"food cords {self.xcor()}, {self.ycor()}")

    def relocate(self, xcor, ycor):
        if fabs(self.xcor() - xcor) <= 0.1 and fabs(self.ycor() - ycor) <= 0.1:
            self.goto(next(self.new_xcor()), next(self.new_ycor()))
            print(f"food cords {self.xcor()}, {self.ycor()}")
            return True

    def new_xcor(self):
        xcor_list = list(range(-600, 601))
        random.shuffle(xcor_list)
        return (i for i in xcor_list if i % MOVE_DISTANCE == 0 and i != self.xcor())

    def new_ycor(self):
        ycor_list = list(range(-340, 341))
        random.shuffle(ycor_list)
        return (i for i in ycor_list if i % MOVE_DISTANCE == 0 and i != self.ycor())
