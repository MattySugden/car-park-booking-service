from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car-park-booking-service.db'
# Initialise database
db = SQLAlchemy(app)


# Database model
class Driver(db.Model):
    __tablename__ = 'registered_drivers'
    driver_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact_number = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String())

    def __repr__(self):
        return '<Name %r>' % self.first_name + ' ' + self.last_name


class Vehicles(db.Model):
    __tablename__ = 'registered_vehicles'
    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_make = db.Column(db.String(50), nullable=False)
    vehicle_model = db.Column(db.String(50), nullable=False)
    vehicle_colour = db.Column(db.String(50), nullable=False)
    vehicle_registration = db.Column(db.String(9), nullable=False, unique=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle_make + ' ' + self.vehicle_model + ' ' + self.vehicle_colour + ' ' + \
            self.vehicle_registration


class Spaces(db.Model):
    __tablename__ = 'parking_spaces'
    space_id = db.Column(db.Integer, primary_key=True)
    space_number = db.Column(db.String(5), nullable=False)

    def __repr(self):
        return '<Space %r>' % self.space_number


class Bookings(db.Model):
    __tablename__ = 'parking_space_bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    booking_date = db.Column(db.DateTime, nullable=False)

    def __repr(self):
        return '<Bookings %r>' % self.booking_date


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/bookings/')
def bookings():
    return render_template("bookings.html")


@app.route('/register/')
def register():
    return render_template("register.html")


@app.route('/vehicle-details/')
def vehicle_details():
    return render_template("vehicle-details.html")


@app.route('/management-console/')
def management_console():
    return render_template("management-console.html")


@app.route('/test-page/')
def test_page():
    try:
        drivers = Driver.query.order_by(Driver.last_name).all()
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    return render_template("test-page.html")


@app.route('/action-confirmation/')
def action_confirmation():
    return render_template("action-confirmation.html")


@app.route('/booking-confirmation/')
def booking_confirmation():
    return render_template("booking-confirmation.html")


@app.route('/registration-summary/')
def profile_summary():
    return render_template("registration-summary.html")


@app.route('/vehicle-summary/')
def vehicle_summary():
    return render_template("vehicle-summary.html")


@app.route('/driver-summary/')
def driver_summary():
    return render_template("driver-summary.html")


if __name__ == '__main__':
    app.run(debug=True)