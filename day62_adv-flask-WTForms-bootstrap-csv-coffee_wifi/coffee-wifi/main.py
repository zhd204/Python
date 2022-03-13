from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import collections

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = URLField('Location URL', validators=[DataRequired(), URL(require_tld=True)])
    open_time = TimeField('Open time', validators=[DataRequired()])
    close_time = TimeField('Close time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', validators=[DataRequired()],
                                choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validate_choice=True)
    wifi_rating = SelectField('Wifi rating', validators=[DataRequired()],
                              choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validate_choice=True)
    power_rating = SelectField('Power rating', validators=[DataRequired()],
                               choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validate_choice=True)
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        newline = f"\n{form.cafe.data}," \
                  f"{form.url.data}," \
                  f"{form.open_time.data.strftime('%I:%M%p')}," \
                  f"{form.close_time.data.strftime('%I:%M%p')}," \
                  f"{form.coffee_rating.data}," \
                  f"{form.wifi_rating.data}," \
                  f"{form.power_rating.data}"
        with open('day62_adv-flask-WTForms-bootstrap-csv-coffee_wifi/coffee-wifi/cafe-data.csv', newline='', mode="a") as f:
            f.write(newline)
        return redirect(url_for('cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day62_adv-flask-WTForms-bootstrap-csv-coffee_wifi/coffee-wifi/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
