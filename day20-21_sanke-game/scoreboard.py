from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.setposition(0, 360)
        self.hideturtle()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read().strip())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}        Highest Score: {self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open('data.txt', mode='w') as f:
            f.write(str(self.high_score))
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 24, "normal"))
