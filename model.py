from flask_sqlalchemy import sqlalchemy

class Driver(db.Model):
    driver_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact_number = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String())

    def __repr__(self):
        return '<Name %r>' % self.first_name + ' ' + self.last_name


class Vehicles(db.Model):
    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_make = db.Column(db.String(50), nullable=False)
    vehicle_model = db.Column(db.String(50), nullable=False)
    vehicle_colour = db.Column(db.String(50), nullable=False)
    vehicle_registration = db.Column(db.String(9), nullable=False, unique=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle_make + ' ' + self.vehicle_model + ' ' + self.vehicle_colour + ' ' + self.vehicle_registration


class Spaces(db.Model):
    space_id = db.Column(db.Integer, primary_key=True)
    space_number = db.Column(db.String(5), nullable=False)

    def __repr(self):
        return '<Space %r>' % self.space_number


class Bookings(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    booking_date = db.Column(db.DateTime, nullable=False)

    def __repr(self):
        return '<Bookings %r>' % self.booking_date
