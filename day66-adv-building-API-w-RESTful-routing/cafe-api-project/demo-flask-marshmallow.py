from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Initialize the Marshmallow extensions
ma = Marshmallow(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # @property
    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "map_url": self.img_url,
    #         "location": self.location,
    #         "seats": self.seats,
    #         "has_toilet": self.has_toilet,
    #         "has_wifi": self.has_wifi,
    #         "has_sockets": self.has_sockets,
    #         "can_take_calls": self.can_take_calls,
    #         "coffee_price": self.coffee_price
    #     }


# Generate marshmallow Schemas from models using SQLAlchemySchema or SQLAlchemyAutoSchema.

class CafeSelectedSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cafe

    # Need to select the fields that want to be included in the JSON data
    id = ma.auto_field()
    name = ma.auto_field()
    location = ma.auto_field()


# Automatically include all fields defined in the SQLAlchemy data model
class CafeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cafe


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all")
def all_():
    all_cafes = db.session.query(Cafe).all()
    cafe_schema = CafeSchema(many=True)  # Specify many=True since there are multiple cafe objects
    # cafe_schema = CafeSelectedSchema(many=True)
    output = cafe_schema.dump(all_cafes)
    print(type(output))
    return jsonify({"cafes": output})


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
