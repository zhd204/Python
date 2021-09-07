from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def quit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=1280, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()
game_is_on = True


while game_is_on:
    screen.update()
    sleep(0.2)
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    snake.move()
    # Detect collision with food.
    if food.relocate(snake.head.xcor(), snake.head.ycor()):
        snake.add_snake()
        scoreboard.score += 1
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 640 or snake.head.xcor() < -640 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        # game_is_on = False
        scoreboard.reset_game()
        snake.reset_snake()
        # scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.snake_body[4:]:
        if snake.head.distance(segment) < 0.001:
            # game_is_on = False
            scoreboard.reset_game()
            snake.reset_snake()
            # scoreboard.game_over()

    screen.onkey(quit_game, "q")

screen.exitonclick()
