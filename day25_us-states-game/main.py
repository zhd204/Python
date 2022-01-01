import turtle
import pandas


def quit_game():
    global game_continue
    game_continue = False


def convert_capitals(words):
    new_words = ""
    words_list = words.split(" ")
    for word in words_list:
        new_words += word.capitalize() + " "

    new_words = new_words.strip()
    return new_words


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.register_shape(image)
screen.setup(width=725, height=491)
turtle.shape(image)
screen.title("U.S. States Game")
screen.listen()

states_pd = pandas.read_csv("50_states.csv")
print(states_pd)
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-300, 240)

states_list = states_pd.state.to_list()

game_continue = True
counter = 0
correct_answers = []
while game_continue:
    user_input = screen.textinput(title=f"{counter}/50 States Correct", prompt="What's another state's name?")
    answer = user_input.title()
    correct_answers.append(answer)
    if answer in states_list:
        xcor = int(states_pd[states_pd.state == answer].x)
        ycor = int(states_pd[states_pd.state == answer].y)
        text.goto(xcor, ycor)
        text.write(answer, align='center', font=('Courier', 10, 'normal'))
        counter += 1

    if counter == len(states_list):
        game_continue = False

    if answer == "Exit":
        game_continue = False

correct_answers_set = set(correct_answers)
all_states_set = set(states_list)

states_to_learn = list(all_states_set - correct_answers_set)
pd_states_to_learn = pandas.DataFrame(states_to_learn)
pd_states_to_learn.to_csv('states_to_learn.csv')

# with open('states_to_learn.csv', mode='w') as f:


