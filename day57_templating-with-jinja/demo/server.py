from flask import Flask, render_template
import random
from datetime import datetime
from utils import guess_func
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    data = guess_func(name)
    return render_template("guess.html", name=data["name"], gender=data["gender"], age=data["age"])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
