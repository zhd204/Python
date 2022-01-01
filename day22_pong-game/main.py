import time
from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from math import fabs
from scoreboard import Scoreboard


def quit_game():
    global is_continue
    is_continue = False


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Pong Game!")
screen.listen()
screen.tracer(0)

score = Scoreboard()

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)

ball = Ball()
screen.onkey(paddle_right.move_up, "o")
screen.onkey(paddle_right.move_down, "l")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(quit_game, "q")

is_continue = True
while is_continue:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (paddle_right.xcor() - ball.xcor() <= 20 and fabs(paddle_right.ycor() - ball.ycor()) <= 30) or \
            (ball.xcor() - paddle_left.xcor() <= 20 and fabs(ball.ycor() - paddle_left.ycor()) <= 30):
        ball.bounce_x()

    # Detect miss with the right paddle
    if ball.xcor() >= 380:
        ball.reset_position()
        score.l_scored()

    # Detect miss with the left paddle
    if ball.xcor() <= -380:
        ball.reset_position()
        score.r_scored()

    score.update_score()
screen.exitonclick()
