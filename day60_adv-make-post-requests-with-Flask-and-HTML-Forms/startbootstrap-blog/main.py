import os

from flask import Flask, render_template, request
from post import Post
import smtplib


def send_email(from_email, password_, to_email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password_)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=f"Subject:User Inquiry!\n\n{message}")


app = Flask(__name__)
post = Post()
blogs = post.get_blogs()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/index')
def index():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:id_num>')
def get_blog(id_num):
    blog = None
    for item in blogs:
        if item['id'] == id_num:
            blog = item
            print(blog['title'])
            break
    return render_template("post.html", blog=blog)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title_message="Contact me")
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message_body = request.form["message"]
        message = f"From: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message_body}"
        my_email = os.environ.get("TESTING_EMAIL")
        my_password = os.environ.get("EMAIL_PASSWORD")
        send_email(to_email=my_email, password_=my_password, from_email=my_email, message=message)
        return render_template("contact.html", title_message="Successfully sent message")


if __name__ == "__main__":
    app.run(debug=True)
