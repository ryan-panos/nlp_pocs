from datetime import datetime

from flaskular.core import db
from flaskular import app

class DateEnteredMixin(object):
    date_entered = db.Column(db.DateTime, default=datetime.utcnow)

class Person(DateEnteredMixin, db.Model):
    "A person that shows up at games from time to time."
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    picture = db.Column(db.String(128))
    games = db.relationship('Game', lazy='dynamic', secondary='players')


#    "A Person on a Team"
players = db.Table('players',
                   db.Column('person_id', db.Integer,
                             db.ForeignKey('people.id'), nullable=False),
                   db.Column('game_id', db.Integer,
                             db.ForeignKey('games.id'), nullable=False),
                   db.Column('team', db.String(1), nullable=False))


class Game(DateEnteredMixin, db.Model):
    "A duel to the death between two teams."
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    winning_team = db.Column(db.String(1))
    players = db.relationship('Person',
                              lazy='dynamic', secondary='players')



# models for which we want to create API endpoints
app.config['API_MODELS'] = {'person': Person}


# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {}
