from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class EditRating(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovie(FlaskForm):
    title = FloatField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
