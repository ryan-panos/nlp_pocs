import os
import json
import datetime

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from flask_restful import reqparse

from flaskular import app

# routing for API endpoints (generated from the models designated as
# API_MODELS)
from flaskular.core import api_manager
from flaskular.watson import *
from flaskular.calling_funcs import *


for model_name, model_class in app.config['API_MODELS'].items():
    app.logger.debug("Registering api for %s", model_class)
    api_manager.create_api(model_class, methods=['GET', 'POST', 'DELETE'])


session = api_manager.session

DEFAULT_INPUT = "sumy_text2_sh.csv"

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

    parser = reqparse.RequestParser()
    parser.add_argument('input_file', location='args', required=False)
    parser.add_argument('is_many', location='args', required=False)
    parser.add_argument('is_target', location='args', required=False)
    # parser.add_argument('is_many', location='args', required=False)
    args = parser.parse_args()

    print " ------------>>>> args: " + str(args)

    if args['input_file'] is not None and len(args['input_file']) > 0:
        print " FOUND input_file:" + args['input_file'] + "|"
        input_file = args['input_file']

    print " testIBM . . .... "

    ## make calls here and return a huge dict

    callStart = datetime.datetime.now()
    ## GOING TO EVENTUALLY GO THROUGH CALLING FUNCs!
    mWatson = MonitorWatsonAPI()
    # result = mWatson.give_all_nlp("A test string of greatness")

    if args['is_many'] is not None:
        print ">=============> args['is_many'] == " + str(args['is_many']) + " so doing MANY! "
        result = {"resp_time" : "Joy!"}

        # result[] = mWatson.get_ibm_service( "sentace about trump that sucks " , emotion)

        # mWatson.get_ibm_service_by_tag( txt_str, "emotion")

        result = get_a_series_of_calls(input_file, ["emotion", "concepts", "dates", "entities", "keywords",
                            "language", "relations", "sentiment",
                                    "taxonomy", "typed_relations"], mWatson.get_ibm_service_by_tag)

        # THE ODD CALLS!   "feeds" microformats publication_date
        # publication_date() got an unexpected keyword argument 'text'
        '''
        microformats, title - only html and url

        '''

    elif args['is_target'] is not None:
        print ">=============> args['is_many'] == " + str(args['is_many']) + " so doing MANY! "
        result = {"resp_time" : "Joy!"}

        # result[] = mWatson.get_ibm_service( "sentace about trump that sucks " , emotion)

        # mWatson.get_ibm_service_by_tag( txt_str, "emotion")

        result = get_a_series_of_calls(input_file, ["emotion", "concepts", "dates", "entities", "keywords",
                            "language", "relations", "sentiment",
                                    "taxonomy", "typed_relations"], mWatson.get_ibm_service_by_tag)

        # THE ODD CALLS!   "feeds" microformats publication_date
        # publication_date() got an unexpected keyword argument 'text'
        '''
        microformats, title - only html and url

        '''
    else:

        result = get_all_vendor_responses(input_file, mWatson.give_all_nlp)

    print "-----> Call took: " + str((datetime.datetime.now() - callStart).total_seconds())

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




