from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drivers.db'
# Initialise database
db = SQLAlchemy(app)


# Database model
class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact_number = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String())

    def __repr__(self):
        return '<Name %r>' % self.first_name + ' ' + self.last_name


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
    return render_template("test-page.html")


if __name__ == '__main__':
    app.run(debug=True)