from datetime import datetime

from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_SERVE_LOCAL'] = True
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.query(BlogPost).get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# NOTE: HTML forms (WTForms included) do not accept PUT, PATCH or DELETE methods.
# So while this would normally be a PUT request (replacing existing data),
# because the request is coming from a HTML form,
# you should accept the edited post as a POST request.
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    edit_mode = request.args.get("edit_mode")
    selected_post = db.session.query(BlogPost).get(post_id)

    # Populate the form from the data
    post_form = CreatePostForm(obj=selected_post)

    # Do below code if only selected fields need to be populated
    # post_form.title.data = selected_post.title

    if post_form.validate_on_submit():
        # Update the data from the form
        post_form.populate_obj(selected_post)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))

    return render_template("make-post.html", form=post_form, mode=edit_mode)


@app.route("/add", methods=["GET", "POST"])
def make_post():
    edit_mode = request.args.get("edit_mode")
    add_post_form = CreatePostForm()

    if add_post_form.validate_on_submit():
        new_post_data = request.form.to_dict()
        # title = add_post_form.title.data
        # subtitle = add_post_form.subtitle.data
        # author = add_post_form.author.data
        # img_url = add_post_form.img_url.data
        # body = add_post_form.body.data
        date = datetime.now().strftime("%B %d, %Y")
        # new_post = BlogPost(title=title,
        #                     subtitle=subtitle,
        #                     date=date,
        #                     body=body,
        #                     author=author,
        #                     img_url=img_url)

        # remove the keys that do not have corresponding columns in the table
        new_post_data.pop("csrf_token")
        new_post_data.pop("submit")

        new_post_data["date"] = date
        new_post = BlogPost(**new_post_data)

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=add_post_form, mode=edit_mode)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(debug=True)
