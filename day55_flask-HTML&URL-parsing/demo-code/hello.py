from flask import Flask
import functools

app = Flask(__name__)


def make_bold(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        bold_value = f"<b>{value}</b>"
        return bold_value

    return inner


def make_emphasis(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        bold_value = f"<em>{value}</em>"
        return bold_value

    return inner


def make_underlined(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        bold_value = f"<u>{value}</u>"
        return bold_value

    return inner


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src=https://media.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif width=200></img>'


# Different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "Bye"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
