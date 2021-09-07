from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-295, 252)
        self.update_score(0, 0)

    def update_score(self, user_level, car_speed):
        self.clear()
        self.write(f"Level: {user_level}\nSpeed: {car_speed}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)



