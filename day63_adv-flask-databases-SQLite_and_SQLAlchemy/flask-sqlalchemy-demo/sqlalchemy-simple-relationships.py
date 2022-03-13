from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts-collection.db'  # Three slashes indicate relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Post -> Category, Many-to-One relationship
# Basic relationship pattern https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html

# Some parts that are required in SQLAlchemy are optional in Flask-SQLAlchemy.
# For instance the table name is automatically set for you unless overridden.
# It’s derived from the class name converted to lowercase and with “CamelCase” converted to “camel_case”.
# To override the table name, set the __tablename__ class attribute.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)  # 'category.id' refer to the id attribute of the category defined in the vey next line
    category = db.relationship('Category', backref=db.backref(
        'posts'))  # "posts" is the name when referring back to the post from category

    def __repr__(self):
        return f"Post {self.title}"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Category {self.name}"


if __name__ == "__main__":
    if not check_database("day63_adv-flask-databases-SQLite_and_SQLAlchemy/flask-sqlalchemy-demo/posts-collection.db"):
        db.create_all()
        print("db created")
    else:
        print("db exists")

    py = Category(name='Python')  # Primary keys are automatically populated if left open.
    new_post = Post(title='Hello Python!', body='Python is pretty cool', category=py)
    db.session.add(py)
    db.session.commit()
    print(py.posts)

    new_post2 = Post(title='Snakes', body='Sssssss')
    py.posts.append(new_post2)  # Back reference to the post collection from category
    db.session.commit()
    print(py.posts)
