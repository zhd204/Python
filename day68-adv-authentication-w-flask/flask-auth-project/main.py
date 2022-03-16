from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, Markup
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    logged_in = current_user.is_authenticated
    return render_template("index.html", logged_in=logged_in)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_pwd = generate_password_hash(password, method="pbkdf2:sha256:80000", salt_length=8)

        if db.session.query(User).filter_by(email=email).first():
            login_msg = Markup("User exists.<br>Please try to login.<br>")
            flash(login_msg)
            return redirect(url_for("login"))
        else:
            new_user = User(name=name, email=email, password=hashed_pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("secrets", name=name))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        existing_user = db.session.query(User).filter_by(email=email).first()
        login_fail_msg = Markup("Login failed.<br>Email and password do not match.<br>")
        if existing_user:
            if check_password_hash(existing_user.password, password):
                logged_in = login_user(existing_user)
                return redirect(url_for("secrets", name=existing_user.name, logged_in=logged_in))
            else:
                flash(login_fail_msg)
        else:
            flash(login_fail_msg)
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    logged_in = request.args.get("logged_in")
    return render_template("secrets.html", name=name, logged_in=logged_in)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static/files",
                               "cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
