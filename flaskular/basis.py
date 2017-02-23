
# from rosette.api import API
from rosette.api import API, DocumentParameters, RosetteException


class MonitorBasisAPI():
    API_KEY = "cfdb0d7990f5c1d2546c61a94cf0a445"

    def __init__(self):
        self.rosette_handle = API(user_key=self.API_KEY)
        # altUrl='https://api.rosette.com/rest/v1/'
        # OPTION: service_url=altUrl

        result = self.rosette_handle.ping()
        print("/ping: ", result)


    def temp_demo(self):
        pass


    def get_basis_sentiment(self, txt_str):
        params = DocumentParameters()
        params["language"] = "eng"

        # Use an HTML file to load data instead of a string
        params.load_document_file(txt_str)
        try:
            result = self.rosette_handle.sentiment(params)
        except RosetteException as e:
            print(e)
        finally:
            print " DONE "





# mba = MonitorBasisAPI()