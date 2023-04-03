# Car Park Booking Service

This web application is for booking a parking space in the DWP office in Leeds.

The application is build with:
- Python3 version 3.11.0
- Flask 2.2.2
- PostgreSQL database
- HTML/CSS web page interface

The code is pushed to GitHub repositiory where the code can be viewed and cloned for developement and to run locally.  The production version of the service is hosted hosted in Heroku cloud and can be access via: https://../...

To run the service locally, clone the application from GitHub repository: https://github.com/MattySugden/car-park-booking-service

## Running the application locally

These following commands are not necessary to run in terminal as *app.run(debug=True)* code in **app.py** replaces the need to run.

To run the code locally, open terminal and cd to the directory where the code was cloned.  Then type:
*python3 -m flask run*

Eg
**MacOS** - Open terminal and type:
export FLASK_APP=hello.py
flask run

**Windows** - Open terminal and type:
set FLASK_APP=hello.py
flask run

The terminal should return a message and quote the http link to run locally in the browser.

The application can be accessed via: http://127.0.0.1:5000

app.py is the main web application file that runs and displays the web application interface and enables functionality.

## Database

The PostgreSQL datbase contains 1 schema that manages 4 tables where the data is stored.
- Table 1 - Registered Drivers
- Table 2 - Registered Vehicles
- Table 3 - Parking Spaces
- Table 4 - Space Bookings

Each table has a primary key set at the unique ID on each table.  

The foreign keys are all matched in the 'Space Bookings' tables to link all data together.

## Front-end Web Application

The front-end of the application had been developed in HTML and CSS. The stylesheet and all images are saved in the /static/ folder.  All the HTML pages are saved in the /templates/ folder.  The styling uses Bootstrap and the templates for each page inherited from base.html.

## Back-end Application

The back-end application is coded in Python3 and uses the Flask 2.2.2 framework.  The main file the runs the application is "app.py"


