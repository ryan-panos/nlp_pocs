
import json
# from rosette.api import API
from rosette.api import API, DocumentParameters, RosetteException
import datetime


class MonitorBasisAPI():
    API_KEY = "cfdb0d7990f5c1d2546c61a94cf0a445"
    DO_NOT_CALL = False

    def __init__(self):
        self.rosette_handle = API(user_key=self.API_KEY)
        # altUrl='https://api.rosette.com/rest/v1/'
        # OPTION: service_url=altUrl

        result = self.rosette_handle.ping()
        print("/ping: ", result)


    def temp_demo(self):
        pass

    # NOT TESTED
    def get_basis_sentiment(self, txt_str):
        params = DocumentParameters()
        params["language"] = "eng"

        # Use an HTML file to load data instead of a string
        params.load_document_string(txt_str)
        try:
            result = self.rosette_handle.sentiment(params)
        except RosetteException as e:
            print(e)
        finally:
            print " DONE "

    # NOT TESTED
    def get_basis_categories(self, txt_str):
        # if self.DO_NOT_CALL == True:
        #     return "POS"

        params = DocumentParameters()
        params["language"] = "eng"

        # Use an HTML file to load data instead of a string
        params.load_document_string(txt_str)

        typed_relations_resp = self.rosette_handle.categories(text=txt_str)

        print " >>> CALLED IBM - typed_relations_resp: " + str(typed_relations_resp)
        return json.dumps(typed_relations_resp)

    def get_basis_service_by_tag(self, txt_str, basis_str):
        '''
            To Be Determined:
            - syntax_dependencies
            - morphology
            - name_translation
            - name_similarity
        '''
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~ going to get_basis_service_by_tag: " + str(basis_str)



        # if ibm_str == "authors":
        #     return self.get_basis_service(txt_str, self.rosette_handle.authors)
        # elif ibm_str == "concepts":
        #     return self.get_basis_service(txt_str, self.rosette_handle.concepts)
        # elif ibm_str == "dates":
        #     return self.get_basis_service(txt_str, self.rosette_handle.dates)
        # elif ibm_str == "emotion":
        #     return self.get_basis_service(txt_str, self.rosette_handle.emotion)
        # elif ibm_str == "feeds":
        #     return self.get_basis_service(txt_str, self.rosette_handle.feeds)
        # elif ibm_str == "keywords":
        #     return self.get_basis_service(txt_str, self.rosette_handle.keywords)
        # elif ibm_str == "microformats":
        #     return self.get_basis_service(txt_str, self.rosette_handle.microformats)
        # elif ibm_str == "publication_date":
        #     return self.get_basis_service(txt_str, self.rosette_handle.publication_date)
        #

        # CURRENT LIST:  "entities", "language", "relationships", "sentences", "sentiment", "syntax_dependencies", "tokens"

        if basis_str == "entities":
            return self.get_basis_service(txt_str, self.rosette_handle.entities)  # also could use  params["genre"] = "social-media"
        elif basis_str == "language":
            return self.get_basis_service(txt_str, self.rosette_handle.language)  #!
        elif basis_str == "relationships":
            return self.get_basis_service(txt_str, self.rosette_handle.relationships)  #!
        elif basis_str == "sentences":
            return self.get_basis_service(txt_str, self.rosette_handle.sentences) #!
        elif basis_str == "sentiment":
            return self.get_basis_service(txt_str, self.rosette_handle.sentiment)
        elif basis_str == "syntax_dependencies":
            return self.get_basis_service(txt_str, self.rosette_handle.syntax_dependencies)
        elif basis_str == "tokens":
            return self.get_basis_service(txt_str, self.rosette_handle.tokens) #!

        # elif ibm_str == "title":
        #     return self.get_basis_service(txt_str, self.rosette_handle.title)
        # elif ibm_str == "typed_relations":
        #     return self.get_basis_service(txt_str, self.rosette_handle.typed_relations)


    def get_basis_service(self, txt_str, basis_func):
        if self.DO_NOT_CALL == True:
            return "POS"
        callStart = datetime.datetime.now()

        params = DocumentParameters()
        params["language"] = "eng"

        # Use an HTML file to load data instead of a string
        params.load_document_string(txt_str)

        # TODO: determine when to use
        # params["content"]  vs load_document_string

        resp = {"return_data": basis_func(params)}

        # print " >>> CALLED IBM - resp: " + str(resp)

        resp_time = (datetime.datetime.now() - callStart).total_seconds()
        resp['resp_time'] = resp_time
        return resp


# mba = MonitorBasisAPI()