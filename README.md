# Flaskular

My stab at combining Angular and Flask. This is based originally on
https://github.com/rxl/angular-flask. It's been:

* Updated with more recent angular-seed.
* Scripts are in the scripts folder
* includes testing config (fixed from angular-seed)
* setup.py for this project

It still contains some bits of the blog demo project that he made; but
i've been removing those.


### How to Get Started

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

3. run the app
> runserver.py

4. create and seed the db (the server must still be running, so open a new terminal window first)
> python manage.py create_db && python manage.py seed_db --seedfile 'data/db_items.json'

5. check out your blog
> http://localhost:8000/blog

