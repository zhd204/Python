from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    # Get the data received in a Flask request
    # https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    # Sending data from HTML form to a Python script in Flask
    # https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
    name = request.form['name']
    password = request.form['password']
    return render_template("login.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)
