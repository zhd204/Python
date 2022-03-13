from flask import Flask, render_template

from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, InputRequired, email, Length
from flask_wtf import FlaskForm

from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), email()])
    password = PasswordField(label="Password", validators=[DataRequired(), InputRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "some secret string"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            # print(login_form.email)
            return render_template("success.html")
        else:
            # print(login_form.email)
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
