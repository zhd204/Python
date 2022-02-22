from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = Post()
blogs = posts.get_blogs()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/post/<int:id_num>')
def get_blog(id_num):
    blog = None
    for item in blogs:
        if item['id'] == id_num:
            blog = item
            print(blog['title'])
            break
    return render_template("post.html", post=blog)


if __name__ == "__main__":
    app.run(debug=True)
