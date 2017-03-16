# NLP PoCs
These scripts are designed to demostrate both the quality and speed of the responses from the NLP vendors currently under review.



### How to Get Started

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)

        (possible start and execute a virtualenv)
        pip install -r requirements.txt
        pip install -e ./
        npm install karma
        npm install karma-ng-scenario
        npm install karma-junit-reporter

3. run the app (from project root dir)

        ./scripts/runserver.py
        
4. check out the site: http://localhost:8000/
        


### Steps to be considered in the future - we are currently not utlizing a DB

5. create and seed the db (the server must still be running, so open a new terminal window first)

        python manage.py create_db && python manage.py seed_db --seedfile 'data/db_items.json'



### Running the tests

Need to make sure the flask server is running. And then run either
`scripts/test.sh` or `scripts/e2e-test.sh`.
