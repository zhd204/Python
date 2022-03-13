from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'  # Three slashes indicate relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    # define class attributes / columns in the table of Book
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.title} - {self.author}"


if __name__ == "__main__":

    if not check_database("day63_adv-flask-databases-SQLite_and_SQLAlchemy/flask-sqlalchemy-demo/new-books-collection.db"):
        db.create_all()
        print("db created")
    else:
        print("db exists")
    # try range(1, 10) at first
    # try range(20, 30) again
    for i in range(20, 30):
        # check if book exists in the db
        isExist = bool(Book.query.filter_by(id=i).first()) or bool(Book.query.filter_by(title=f"Book_{i}").first())
        if not isExist:
            new_book = Book(id=i, title=f"Book_{i}", author=f"Author_{i}", rating=random.uniform(0.0, 10.0))
            db.session.add(new_book)
    db.session.commit()

    # Read all books
    all_books = Book.query.all()
    print(type(all_books))
    print(f"All books:\n{all_books}\n")

    # Select book by title
    book = Book.query.filter_by(title="Book_21").first()
    print(f"Selected book:\n{book}\n")

    # Select a book by ID
    # Update the selected book
    book_id = 29
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Book_29_Updated"
    db.session.commit()

    # Read the updated book
    book_id = 29
    book_updated = Book.query.get(book_id)
    print(f"Updated book:\n{book_updated}\n")

    # Delete a book
    book_id = 25
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    # Read all books after the deletion
    all_books = Book.query.all()
    print(f"All books after deletion:\n{all_books}\n")
