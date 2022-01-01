from turtle import Screen, Turtle
from time import sleep


def turn_left():
    segments[0].left(90)


def turn_right():
    segments[0].right(90)


def quit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=1280, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

segments = []
interval = 20
xcor = 0
for _ in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.shapesize(stretch_wid=0.95, stretch_len=0.95)
    segment.penup()
    segment.goto(xcor, 0)
    segments.append(segment)
    xcor -= interval

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    if segments[0].xcor() > 560 or segments[0].xcor() < -560 or segments[0].ycor() > 300 or segments[0].ycor() < -300:
        turn_left()
    for seg_index in range(len(segments) - 1, 0, -1):
        xcor = segments[seg_index - 1].xcor()
        ycor = segments[seg_index - 1].ycor()
        segments[seg_index].goto(xcor, ycor)
    segments[0].forward(20)
    screen.onkey(quit_game, "q")


screen.exitonclick()