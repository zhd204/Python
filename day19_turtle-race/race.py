from turtle import Turtle, Screen
import random

turtles = []
colors = ["red", "orange", "black", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("azure3")
screen.title("Welcome to the turtle race game!")

# Setting up user interface at the beginning
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color from the following:\n"
                                   "red, orange, black, green, blue, purple: ").lower()
while True:
    if user_bet not in colors:
        user_bet = screen.textinput(title="Make your bet",
                                    prompt="Invalid entry. Enter a color from the following:\n"
                                           "red, orange, black, green, blue, purple: ").lower()
    else:
        break

# Setting up turtles at the starting line
y_cor_interval = int(screen.window_height() * 0.5 / (len(colors) - 1))
y_cor = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y_cor)
    y_cor += y_cor_interval
    turtles.append(turtle)


# Setting up the finishing line
flag1 = Turtle(shape="square")
flag1.penup()
flag1.setposition(200, 150)

flag2 = Turtle(shape="square")
flag2.penup()
flag2.setposition(200, 150)
flag2.pendown()
flag2.pensize(width=6)
flag2.setheading(270)
flag2.speed(0)
flag2.forward(300)

# Running the race
winners = []
is_continue = True
while is_continue:
    a = 200
    for turtle in turtles:
        if turtle.xcor() >= a:
            a = turtle.xcor()
            winners.append(turtle)
            is_continue = False
        else:
            turtle.forward(random.randint(0, 5))

# Setting up the group result display
result_str = ""
for turtle in turtles:
    result_str = f"Turtle {turtle.color()[0]}: {turtle.xcor()}\n\n" + result_str

result_all = Turtle()
result_all.penup()
result_all.setposition(-25, -100)
result_all.hideturtle()
result_all.write(arg=result_str, align='center', font=("Arial", 12, "bold"))

# Setting up the final winner and bet result display
final_winner_str = "The winner is:\n"
for winner in winners:
    final_winner_str += f"\tTurtle {winner.color()[0]}: {winner.xcor()}\n\n"

if user_bet in final_winner_str:
    result_user = "You win!✌️\n\n"
else:
    result_user = "You lose ☹️. Try again!\n\n"

final_str = final_winner_str + result_user

result_winner = Turtle()
result_winner.penup()
result_winner.pencolor("red")
result_winner.setposition(-25, 75)
result_winner.hideturtle()
result_winner.write(arg=final_str, align='center', font=("Arial", 16, "bold"))


screen.exitonclick()
