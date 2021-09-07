from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()
        self.level = 0

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        self.reach_finish_line()

    def reset_position(self):
        self.goto(0, -280)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.level += 1
            self.reset_position()
            print(f"current level is: {self.level}")

