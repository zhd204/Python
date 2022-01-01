import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def quit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Welcome to Turtle Crossing!")
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
score = Scoreboard()

game_is_on = True
cycle_counter = 0
update_cycle = 10

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if update_cycle > player.level * 2:
        if cycle_counter % (update_cycle - player.level * 2) == 0:
            car_manager.add_car()
    # player keeps track of levels, level up everytime the player crosses the street
    car_manager.car_forward(player.level)
    car_manager.remove_car()
    cycle_counter += 1
    score.update_score(player.level, car_manager.car_average_speed())
    screen.onkey(player.move_up, "w")
    screen.onkey(quit_game, "q")
    # collision detection monitor by each individual car
    if car_manager.collision(player.xcor(), player.ycor()):
        score.game_over()
        quit_game()

screen.exitonclick()
