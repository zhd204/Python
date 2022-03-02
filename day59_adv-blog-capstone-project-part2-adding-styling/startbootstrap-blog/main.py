from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()
blogs = post.get_blogs()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/index')
def index():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:id_num>')
def get_blog(id_num):
    blog = None
    for item in blogs:
        if item['id'] == id_num:
            blog = item
            print(blog['title'])
            break
    return render_template("post.html", blog=blog)


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
