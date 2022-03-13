from pprint import pprint

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from app_models import db, Movie
from utils import check_database
from app_forms import EditRating, AddMovie
from data_source import MovieSearch
from sqlalchemy import asc, desc, func

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-store.db'  # Three slashes indicate relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(
        asc('rating')).all()  # By default, the ordering is ascending.No need to apply asc() function
    # Getting the count of existing rows. Both ways work.
    # row_count = db.session.query(Movie).count()
    row_count = db.session.query(func.count(Movie.id)).scalar()
    count = len(all_movies)
    print(type(all_movies))
    print(count)

    if row_count > 0:
        index = row_count
        for movie in all_movies:
            movie.ranking = index
            index -= 1
        db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_rating_form = EditRating()
    movie_id = request.args.get("movie_id")
    current_movie = db.session.query(Movie).get(movie_id)
    if not current_movie:
        movie_details = MovieSearch().get_details(movie_id)
        new_movie = Movie(id=movie_id,
                          title=movie_details["title"],
                          year=movie_details["release_date"],
                          description=movie_details["overview"],
                          img_url=MovieSearch().get_poster_url(poster_path=movie_details["poster_path"], size_index=3))
        db.session.add(new_movie)
        db.session.commit()
        current_movie = db.session.query(Movie).get(movie_id)

    if edit_rating_form.validate_on_submit():
        current_movie.rating = float(edit_rating_form.rating.data)
        current_movie.review = edit_rating_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=current_movie, form=edit_rating_form)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        add_movie_form = AddMovie()
        return render_template("edit.html", form=add_movie_form)
    elif request.method == "POST":
        search_keyword = request.form.get("title")
        search_results = MovieSearch().get_results(search_keyword)["results"]

        return render_template("select.html", results=search_results)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    movie_to_delete = db.session.query(Movie).get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    if not check_database("day64-adv-top-100-movies/movie-project/movies-store.db"):
        db.create_all()
        print("db created")
    else:
        print("db exists")
    app.run(debug=True)
