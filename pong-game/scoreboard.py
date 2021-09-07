from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def l_scored(self):
        self.l_score += 1

    def r_scored(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.write(f"Left Player: {self.l_score} vs Right Player: {self.r_score}",
                   move=False, align="center", font=('Courier', 24, "normal"))
