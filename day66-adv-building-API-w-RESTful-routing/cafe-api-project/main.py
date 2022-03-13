from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)  # location
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)  # has_toilet
    has_wifi = db.Column(db.Boolean, nullable=False)  # has_wifi
    has_sockets = db.Column(db.Boolean, nullable=False)  # has_sockets
    can_take_calls = db.Column(db.Boolean, nullable=False)  # can_take_calls
    coffee_price = db.Column(db.String(250), nullable=True)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.img_url,
            "image_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    print(all_cafes)
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all")
def all_():
    all_cafes = db.session.query(Cafe).all()

    # return jsonify(json_list=[cafe.serialize for cafe in all_cafes])
    return jsonify(json_list=[cafe.to_dict() for cafe in all_cafes])


@app.route("/random")
def random_():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    # return jsonify(json_list=[cafe.serialize for cafe in all_cafes])
    return jsonify(random_cafe.serialize)


@app.route("/search")
def search():
    all_cafes = db.session.query(Cafe).all()
    loc_parameter = request.args.get("loc")
    cafe_list = [cafe.serialize for cafe in all_cafes if cafe.location.lower() == loc_parameter.lower()]
    if cafe_list:
        return jsonify(cafe_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_():
    # new_cafe = Cafe(
    #     name=request.form.get("name"),
    #     map_url=request.form.get("map_url"),
    #     img_url=request.form.get("img_url"),
    #     location=request.form.get("loc"),
    #     seats=request.form.get("seats"),
    #     has_toilet=bool(request.form.get("toilet")),
    #     has_wifi=bool(request.form.get("wifi")),
    #     has_sockets=bool(request.form.get("sockets")),
    #     can_take_calls=bool(request.form.get("calls")),
    #     coffee_price=request.form.get("coffee_price")
    # )

    # https://tedboy.github.io/flask/generated/generated/werkzeug.ImmutableMultiDict.html
    request_response = request.form.to_dict()  # This is the to_dict method from werkzeug.ImmutableMultiDict object
    for k, v in request_response.items():
        if v.lower() == "true":
            request_response[k] = True
        elif v.lower() == "false":
            request_response[k] = False

    # convert the dictionary from using parameters as keys to using model fields as keys
    # vey stupid
    cafe_data = {}
    for k in request_response.keys():
        if k.lower() == "loc":
            cafe_data['location'] = request_response[k]
        elif k.lower() in ["toilet", "wifi", "sockets"]:
            cafe_data[f"has_{k.lower()}"] = request_response[k]
        elif k.lower() == "calls":
            cafe_data["can_take_calls"] = request_response[k]
        else:
            cafe_data[k] = request_response[k]

    new_cafe = Cafe(**cafe_data)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:coffee_id>", methods=["PATCH"])
def update_price(coffee_id):
    updated_price = request.args.get("new_price")
    # id is the primary key
    coffee_to_update = db.session.query(Cafe).get(coffee_id)
    # # In case there is need to search the object by other attributes (column names) such as name
    # # Not used in this script
    # try:
    #     coffee_test = db.session.query(Cafe).filter_by(name="Alaska Coffee Roasting").first()
    #     print(coffee_test)
    # except Exception as err:
    #     print(err)
    if coffee_to_update:
        coffee_to_update.coffee_price = updated_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:coffee_id>", methods=["DELETE"])
def report_closed(coffee_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        coffee_to_delete = db.session.query(Cafe).get(coffee_id)
    else:
        return jsonify({"error": "Sorry, that is not allowed. Make sure you have the correct api_key."}), 403

    if coffee_to_delete:
        db.session.delete(coffee_to_delete)
        db.session.commit()
        return jsonify({"success": "Successfully delete the record."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
