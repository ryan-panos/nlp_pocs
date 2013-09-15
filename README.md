# Flaskular

My stab at combining Angular and Flask. This is based originally on
https://github.com/rxl/angular-flask. It's been:

* Updated with more recent angular-seed.
* Scripts are in the scripts folder
* includes testing config (fixed from angular-seed)
* setup.py for this project

It still contains some bits of the blog demo project that he made; but
I've been removing those.


## What's included

* Flask
* Flask-SQLAlchemy
* Bootstrap 3
* flask-restless
* Angular (from angular-seed)
** HTML5 mode (links look like `/about` rather than `#/about`

### How to Get Started

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)

        pip install -r requirements.txt
        pip install -e ./
        npm install karma
        npm install karma-ng-scenario
        npm install karma-junit-reporter

3. run the app

        runserver.py

4. create and seed the db (the server must still be running, so open a new terminal window first)

        python manage.py create_db && python manage.py seed_db --seedfile 'data/db_items.json'

5. check out the site: http://localhost:8000/

### Running the tests

Need to make sure the flask server is running. And then run either
`scripts/test.sh` or `scripts/e2e-test.sh`.
