from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
STEP_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.penup()
        self.goto(xcor, ycor)
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        self.forward(STEP_DISTANCE)

    def move_down(self):
        self.backward(STEP_DISTANCE)
