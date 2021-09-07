from turtle import Turtle
import random
import math

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    class Car(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.penup()
            self.color(random.choice(COLORS))
            self.goto(300, random.randint(-250, 250))
            self.setheading(180)
            self.speed = STARTING_MOVE_DISTANCE

        def move(self, speed_factor):
            self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * speed_factor
            self.forward(self.speed)

        def car_reach_end(self):
            if self.xcor() <= -320:
                return True

        def collision_detection(self, player_xcor, player_ycor):
            # Use 20 or lower for x axis detection to have some overlap when the collision is detected.
            if math.fabs(self.ycor() - player_ycor) <= 20 \
                    and math.fabs(self.xcor() - player_xcor) <= 20:
                print(f"Collision with {self.color()[0]} car")
                print(f"Car position: {self.xcor()}, {self.ycor()}")
                print(f"Player position: {player_xcor, player_ycor}")
                return True

    def __init__(self):
        self.inventory = []

    def add_car(self):
        car = self.Car()
        self.inventory.append(car)

    def remove_car(self):
        if len(self.inventory) != 0:
            for car in self.inventory:
                if car.car_reach_end():
                    self.inventory.remove(car)

    def car_forward(self, speed_factor):
        for car in self.inventory:
            car.move(speed_factor)

    def collision(self, player_xcor, player_ycor):
        if any(map(lambda x: x.collision_detection(player_xcor, player_ycor), self.inventory)):
            return True

    def car_average_speed(self):
        total = 0
        for car in self.inventory:
            total += car.speed

        return round(total / len(self.inventory), 1)