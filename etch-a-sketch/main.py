from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(5)


def clockwise():
    tim.right(5)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, key='W')
screen.onkey(move_backwards, key='S')
screen.onkey(counter_clockwise, key='A')
screen.onkey(clockwise, key='D')
screen.onkey(clear_drawing, key='C')
screen.exitonclick()
