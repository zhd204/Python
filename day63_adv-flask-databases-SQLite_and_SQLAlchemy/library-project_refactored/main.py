from flask import Flask, render_template, request, redirect, url_for
from utils import check_database
from app_models import Book, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-store.db'  # Three slashes indicate relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


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
