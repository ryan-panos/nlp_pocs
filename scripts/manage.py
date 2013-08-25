import os
import json
from opster import command, dispatch
import requests

from flaskular.core import db


def create_sample_db_entry(api_endpoint, payload):
    url = 'http://localhost:8000/' + api_endpoint
    r = requests.post(url, data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
    print r.text


@command()
def create_db():
    db.create_all()
    print "DB created!"


@command()
def drop_db():
    db.drop_all()
    print "DB deleted!"


@command()
def seed_db(seedfile):
    with open(seedfile, 'r') as f:
        seed_data = json.loads(f.read())
    for item_class in seed_data:
        items = seed_data[item_class]
        print items
        for item in items:
            print item
            create_sample_db_entry('api/' + item_class, item)
    print "\nSample data added to database!"


if __name__ == '__main__':
    dispatch()
