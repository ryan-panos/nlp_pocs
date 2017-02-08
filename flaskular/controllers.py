import os
import json

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from flask_restful import reqparse

from flaskular import app

# routing for API endpoints (generated from the models designated as
# API_MODELS)
from flaskular.core import api_manager


for model_name, model_class in app.config['API_MODELS'].items():
    app.logger.debug("Registering api for %s", model_class)
    api_manager.create_api(model_class, methods=['GET', 'POST', 'DELETE'])


session = api_manager.session

DEFAULT_INPUT="THIS default file!"

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
@app.route('/contact')
@app.route('/people')
def basic_pages(**kwargs):
    return send_file('static/index.html')


@app.route('/api/testIBM')
def test_ibm(**kwargs):
    input_file = DEFAULT_INPUT

    # parser = reqparse.RequestParser()
    # parser.add_argument('input_file', location='args', required=False)
    # args = parser.parse_args()
    #
    # if args['input_file'] is None or len(args['input_file']) == 1:
    #     input_file = DEFAULT_INPUT

    print " testIBM . . .... "

    ## make calls here and return a huge dict

    # return send_file('static/test_poc.html')
    # return render_template('static/test_poc.html', input_file=input_file)

    result = {
        'escalate': 'True',
        'NYES!!': 'PART!'
              }
    return json.dumps(result)


# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists
from sqlalchemy.sql import exists

crud_url_models = app.config['CRUD_URL_MODELS']


@app.route('/<model_name>/')
@app.route('/<model_name>/<item_id>')
def rest_pages(model_name, item_id=None):
    if model_name in crud_url_models:
        model_class = crud_url_models[model_name]
        if item_id is None or session.query(
                exists().where(
                    model_class.id == item_id)).scalar():
            return send_file('static/index.html')
    abort(404)


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return send_file('static/index.html'), 404
