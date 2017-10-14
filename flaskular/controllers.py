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
from flaskular.basis import *
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

# temp
IBM = "IBM"
BASIS = "Basis"


def get_params():
    parser = reqparse.RequestParser()
    parser.add_argument('input_file', location='args', required=False)
    parser.add_argument('is_many', location='args', required=False)
    parser.add_argument('is_target', location='args', required=False)
    parser.add_argument('selected_vendor', location='args', required=False)
    # parser.add_argument('is_many', location='args', required=False)
    return parser.parse_args()

@app.route('/api/testIBM')
def test_ibm(**kwargs):

    input_file = DEFAULT_INPUT

    # parser = reqparse.RequestParser()
    # parser.add_argument('input_file', location='args', required=False)
    # parser.add_argument('is_many', location='args', required=False)
    # parser.add_argument('is_target', location='args', required=False)
    # parser.add_argument('is_many', location='args', required=False)
    args = get_params()

    print " ------------>>>> args: " + str(args)

    if 'selected_vendor' in args and args['selected_vendor'] is not None and args['selected_vendor'] in [BASIS, IBM]:
        print " YES IN LIST?   " + args['selected_vendor']
        vendor_used = args['selected_vendor']
    else:
        vendor_used = IBM
        print "using IBM bc ***NOT IN LIST*** so bc dont understand selected_vendor  -> testIBM . . .... " + str(args['selected_vendor'])

    return do_tests(vendor_used, args)

    ## make calls here and return a huge dict


def do_tests(vendor_used, args):
    input_file = DEFAULT_INPUT

    callStart = datetime.datetime.now()
    if args['input_file'] is not None and len(args['input_file']) > 0:
        print " FOUND input_file:" + args['input_file'] + "|"
        input_file = args['input_file']
    else:
        print " Sticking w defaul input file: " + str(input_file)

    ## take this from param?  vendorAPI?

    # TODO do conditional!!!!
    # if vendor_used == BASIS:
    # else:
    mWatson = MonitorWatsonAPI()
    # basisAPI = MonitorBasisAPI()
    # result = mWatson.give_all_nlp("A test string of greatness")

    if args['is_many'] is not None:
        print ">=============> args['is_many'] == " + str(args['is_many']) + " so doing MANY! "
        # result = {"resp_time" : "Joy!"} # moot - debug?

        if vendor_used == IBM:
            print " Yes doing many IBM!!"
            result = get_a_series_of_calls(input_file, ["author", "emotion", "concepts", "dates", "entities", "keywords",
                            "language", "relations", "sentiment",

                                "taxonomy", "typed_relations"], mWatson.get_ibm_service_by_tag)




            print "#### ALL RETURN FROM IBM: " + str(result)

            # one_resp[service_str] = get_service_by_tag(row[content_idx], service_str)
            # vendor_response.append(one_resp)

            # get_one_vendor_responses(input_file,   , function_options=[sentiment=1])

            result = get_a_vendor_response_all_file(input_file, mWatson.get_ibm_entities, use_output_key="entities")
            print "#### JUST ENTITIES RETURN FROM IBM: " + str(result)


        elif vendor_used == BASIS:
            print " \n\n\n --------============ DOING Basis . . ."
            result = get_a_series_of_calls(input_file, [ "entities", "language", "relationships", "sentences",
                                     "sentiment", "syntax_dependencies", "tokens"], basisAPI.get_basis_service_by_tag)

        else:
            print " %% Venor unknown?? "
        '''
        # No response thus far
        # author
        # microformats

        # Todo Services
            # Targeted Emotion - COMING SOON!


        publication_date, microformats, title, text(cleaned) and text(raw) - only html and url!!

        feeds SAYS in API that text should work but does not!

        TODO: targeted_sentiment
        ADDED PARAM REQUIRED: <targets	list>	List of target phrases. The service will return sentiment information
                            for each phrase that is found in the source text. Supports up to 20 phrases.

        '''

    elif args['is_target'] is not None:
        print ">=============> args['is_many'] == " + str(args['is_many']) + " so doing MANY! "

        if vendor_used == IBM:
            result = get_a_series_of_calls(input_file, ["emotion", "concepts", "dates", "entities", "keywords",
                            "language", "relations", "sentiment",
                                    "taxonomy", "typed_relations"], mWatson.get_ibm_service_by_tag)

        elif vendor_used == BASIS:
            print " \n\n\n --------============ DOING Basis . . ."
            result = get_a_series_of_calls(input_file, [ "entities", "language", "relationships", "sentences",
                                     "sentiment", "syntax_dependencies", "tokens"], basisAPI.get_basis_service_by_tag)

        else:
            print " %% Venor unknown?? "

        # THE ODD CALLS!   "feeds" microformats publication_date
        # publication_date() got an unexpected keyword argument 'text'
        '''
        microformats, title - only html and url

        '''
    else:
        print "DOING IBM ALL?? "
        result = get_a_vendor_response_all_file(input_file, mWatson.give_all_nlp)

    print "---232--> Call took: " + str((datetime.datetime.now() - callStart).total_seconds())

    # result["selected_vendor"] = vendor_used
    # print "returning: " + str(json.dumps(result))

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




