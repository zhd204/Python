from flask import Flask
import random

ref = random.randint(0, 9)
print(ref)

app = Flask(__name__)


@app.route("/")
def root():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<div style="text-align: center">' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif width=300></img>' \
           '</div>'


@app.route("/<int:number>")
def guess_number(number):
    if number > ref:
        return '<h1 style="color: purple" align="center">Too high, try again!</h1>' \
               '<div style="text-align: center">' \
               '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width=300></img>' \
               '</div>'
    elif number < ref:
        return '<h1 style="color: red" align="center">Too low, try again!</h1>' \
               '<div style="text-align: center">' \
               '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif width=300></img>' \
               '</div>'
    else:
        return '<h1 style=style="color: green" align="center">You found me!</h1>' \
               '<div style="text-align: center">' \
               '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif width=300></img>' \
               '</div>'


if __name__ == "__main__":
    app.run(debug=True)
