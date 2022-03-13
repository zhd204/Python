from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


def check_database(db_path=None):
    from urllib.request import pathname2url
    import sqlite3

    try:
        db_uri = f"file:{pathname2url(db_path)}?mode=rw"
        conn = sqlite3.connect(db_uri, uri=True)
        conn.close()
        return True
    except sqlite3.OperationalError as err:
        print(err)
        return False


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-store.db'  # Three slashes indicate relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.id}: <{self.title}> by {self.author} with rating({self.rating})"


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_info = {
            "title": request.form["bk_name"],
            "author": request.form["bk_author"],
            "rating": float(request.form["bk_rating"]),
        }
        new_book = Book(title=book_info['title'], author=book_info['author'], rating=book_info['rating'])
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:bk_id>", methods=["GET", "POST"])
def edit_rating(bk_id):
    current_book = Book.query.get(bk_id)
    if request.method == "POST":
        print(request.form["bk_rating"])
        current_book.rating = request.form["bk_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", book=current_book)


@app.route("/<int:bk_id>")
def delete_(bk_id):
    book = Book.query.get(bk_id)

    try:
        book = Book.query.get(bk_id)
        db.session.delete(book)
        db.session.commit()
    except Exception as err:
        print(err)

    return redirect(url_for("home"))


if __name__ == "__main__":
    if not check_database("day63_adv-flask-databases-SQLite_and_SQLAlchemy/library-project/books-store.db"):
        db.create_all()
        print("db created")
    else:
        print("db exists")
    app.run(debug=True)
