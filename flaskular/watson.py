import json
from watson_developer_cloud import AlchemyLanguageV1
import datetime

class MonitorWatsonAPI():
    API_KEY = "d764df8cc016116fe8d2559e52a7474dab6103d4"
    TECH_ADMIN_API_KEY = "e581d5843a8e54af4a0b04ab2619cccde2dae747"
    OLD_RP_API_KEY = "c4eee5a628ea2243350787a04b924bb21ecb6f7e"
    BEN_API_KEY = "b8db92daa6a6ca79bb61c0938babe873de0ed914"
    DO_NOT_CALL = False

    def __init__(self):
        self.alchemy_handle = AlchemyLanguageV1(api_key=MonitorWatsonAPI.API_KEY)

    def give_all_nlp(self, content_txt):
        callStart = datetime.datetime.now()
        return_data={
            "orginal_text":content_txt
        }

        # sent = self.get_ibm_sentiment(content_txt)
        # # Check for error?
        # if sent is not None:
        #     return_data['sentiment'] = sent

        # alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
        # return_data['sentiment'] = alchemy_language.sentiment(text=content_txt)
        # return_data['entities'] = alchemy_language.entities(text=content_txt)
        # return_data['sentiment'] = alchemy_language.sentiment(text=content_txt)
        # return_data['entities'] = alchemy_language.entities(text=content_txt)
        #
        # return_data['sentiment'] = alchemy_language.sentiment(text=content_txt)
        # return_data['entities'] = alchemy_language.entities(text=content_txt)
        # return_data['sentiment'] = alchemy_language.sentiment(text=content_txt)
        # return_data['entities'] = alchemy_language.entities(text=content_txt)
        #
        return_data['full_response'] = self.alchemy_handle.combined(text=content_txt,
                                         extract='authors, concepts, dates, doc-emotion, entities,'
                                                 + ' feeds, keywords, pub-date, relations, typed-rels,'
                                                 + ' doc-sentiment, taxonomy, title')

        # 'sentiment,entities,keyword
        #   max_items	    integer	The maximum number of results to return for each applicable extract operation
        #   showSourceText	integer	Set this to 1 to include the source text in the response
        #
        resp_time = (datetime.datetime.now() - callStart).total_seconds()
        return_data['resp_time'] = resp_time

        return return_data

    def get_ibm_service_by_tag(self, txt_str, ibm_str):

        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~ going to get_ibm_service_by_tag: " + str(ibm_str)

        if ibm_str == "authors":
            return self.get_ibm_service(txt_str, self.alchemy_handle.authors)
        elif ibm_str == "concepts":
            return self.get_ibm_service(txt_str, self.alchemy_handle.concepts)
        elif ibm_str == "dates":
            return self.get_ibm_service(txt_str, self.alchemy_handle.dates)
        elif ibm_str == "emotion":
            return self.get_ibm_service(txt_str, self.alchemy_handle.emotion)
        elif ibm_str == "entities":
            return self.get_ibm_service(txt_str, self.alchemy_handle.entities)
        elif ibm_str == "feeds":
            return self.get_ibm_service(txt_str, self.alchemy_handle.feeds)
        elif ibm_str == "keywords":
            return self.get_ibm_service(txt_str, self.alchemy_handle.keywords)
        elif ibm_str == "language":
            return self.get_ibm_service(txt_str, self.alchemy_handle.language)
        elif ibm_str == "microformats":
            return self.get_ibm_service(txt_str, self.alchemy_handle.microformats)
        elif ibm_str == "publication_date":
            return self.get_ibm_service(txt_str, self.alchemy_handle.publication_date)
        elif ibm_str == "relations":
            return self.get_ibm_service(txt_str, self.alchemy_handle.relations)
        elif ibm_str == "sentiment":
            return self.get_ibm_service(txt_str, self.alchemy_handle.sentiment)
        elif ibm_str == "taxonomy":
            return self.get_ibm_service(txt_str, self.alchemy_handle.taxonomy)
        elif ibm_str == "title":
            return self.get_ibm_service(txt_str, self.alchemy_handle.title)
        elif ibm_str == "typed_relations":
            return self.get_ibm_service(txt_str, self.alchemy_handle.typed_relations)


    def get_ibm_service(self, txt_str, ibm_func):
        if self.DO_NOT_CALL == True:
            return "POS"
        callStart = datetime.datetime.now()
        resp = {"return_data": ibm_func(text=txt_str)}

        # print " >>> CALLED IBM - resp: " + str(resp)

        resp_time = (datetime.datetime.now() - callStart).total_seconds()
        resp['resp_time'] = resp_time
        return resp



    # Todo note the second param required!
    def get_ibm_targeted_sentiment(self, txt_str, targeted_sentiment_resp_ls):
        if self.DO_NOT_CALL == True:
            return "POS"

        targeted_sentiment_resp = self.alchemy_handle.targeted_sentiment(text=txt_str, targets=targeted_sentiment_resp_ls)

        print " >>> CALLED IBM - targeted_sentiment_resp: " + str(targeted_sentiment_resp)
        return json.dumps(targeted_sentiment_resp)



    def get_ibm_typed_relations(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        typed_relations_resp = self.alchemy_handle.typed_relations(text=txt_str)

        print " >>> CALLED IBM - typed_relations_resp: " + str(typed_relations_resp)
        return json.dumps(typed_relations_resp)

    def get_ibm_authors(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"
        callStart = datetime.datetime.now()
        auth_resp = {'data': self.alchemy_handle.authors(text=txt_str)}

        print " >>> CALLED IBM - auth_resp: " + str(auth_resp)

        resp_time = (datetime.datetime.now() - callStart).total_seconds()
        auth_resp['resp_time'] = resp_time
        return json.dumps(auth_resp)

    def get_ibm_concepts(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        concepts_resp = self.alchemy_handle.concepts(text=txt_str)

        print " >>> CALLED IBM - concepts_resp: " + str(concepts_resp)
        return json.dumps(concepts_resp)

    def get_ibm_dates(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        dates_resp = self.alchemy_handle.dates(text=txt_str)

        print " >>> CALLED IBM - dates_resp: " + str(dates_resp)
        return json.dumps(dates_resp)


    def get_ibm_emotion(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        emotion_resp = self.alchemy_handle.emotion(text=txt_str)

        print " >>> CALLED IBM - emotion_resp: " + str(emotion_resp)
        return json.dumps(emotion_resp)

    def get_ibm_entities(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        entities_resp = self.alchemy_handle.entities(text=txt_str)

        print " >>> CALLED IBM - entities_resp: " + str(entities_resp)
        return json.dumps(entities_resp)

    def get_ibm_feeds(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        feeds_resp = self.alchemy_handle.feeds(text=txt_str)

        print " >>> CALLED IBM - feeds_resp: " + str(feeds_resp)
        return json.dumps(feeds_resp)

    ###
    def get_ibm_keywords(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        keywords_resp = self.alchemy_handle.keywords(text=txt_str)

        print " >>> CALLED IBM - keywords_resp: " + str(keywords_resp)
        return json.dumps(keywords_resp)

    def get_ibm_language(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        language_resp = self.alchemy_handle.language(text=txt_str)

        print " >>> CALLED IBM - language_resp: " + str(language_resp)
        return json.dumps(language_resp)


    def get_ibm_microformats(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

            microformats_resp = self.alchemy_handle.microformats(text=txt_str)

        print " >>> CALLED IBM - microformats_resp: " + str(microformats_resp)
        return json.dumps(microformats_resp)

    def get_ibm_publication_date(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        publication_date_resp = self.alchemy_handle.publication_date(text=txt_str)

        print " >>> CALLED IBM - publication_date_resp: " + str(publication_date_resp)
        return json.dumps(publication_date_resp)

    def get_ibm_relations(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        relations_resp = self.alchemy_handle.relations(text=txt_str)

        print " >>> CALLED IBM - relations_resp: " + str(relations_resp)
        return json.dumps(relations_resp)


    ##


    def get_ibm_sentiment(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        sentiment_resp = self.alchemy_handle.sentiment(text=txt_str)

        print " >>> CALLED IBM - sentiment_resp: " + str(sentiment_resp)
        return json.dumps(sentiment_resp)




    def get_ibm_taxonomy(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        taxonomy_resp = self.alchemy_handle.taxonomy(text=txt_str)

        print " >>> CALLED IBM - taxonomy_resp: " + str(taxonomy_resp)
        return json.dumps(taxonomy_resp)

    def get_ibm_title(self, txt_str):
        if self.DO_NOT_CALL == True:
            return "POS"

        title_resp = self.alchemy_handle.title(text=txt_str)

        print " >>> CALLED IBM - feeds_resp: " + str(title_resp)
        return json.dumps(title_resp)

    # def get_ibm_sentiment(self, txt_str):
    #     if self.DO_NOT_CALL == True:
    #         return "POS"
    #
    #     sent_resp = self.alchemy_handle.sentiment(text=txt_str)
    #
    #     print " >>> CALLED IBM - sent_resp: " + str(sent_resp)
    #     return json.dumps(sent_resp)



'''

Services available - Per IBM Rep (Jacob Ellison <jellison@us.ibm.com>):

    Emotion & Sentiment analysis - Both are available as Watson APIs under the AlchemyLanguage Service
    Sentence/Document Level Sentiment/Emotion (DLS/E) - Both are available as Watson APIs under the AlchemyLanguage Service
    Entity Level Sentiment/Emotion (ELS/E) - Both are available as Watson APIs under the AlchemyLanguage service
    Relation Extraction (RelEx) - Available as a Watson API under the AlchemyLanguage service
    Named Entity Recognition (NER) - Available as a Watson API under the AlchemyLanguage service
    Named Entity Disambiguation (NED) - Included in the results of NER API Calls.
    Topic Extraction (TopEx) - Taxonomy, Concept Tagging and Keyword Extraction with relevance scores,
       all available under the AlchemyLanguage service are probably the closest proxy to Topic Extraction.

    Paragraph Splitting (PSplit) - Not available
    Co-reference Resolution (CoRef) - Not available
    Concept Level Sentiment/Emotion (CLS/E) - Not available.


Summarization (Summ) - Not Available

'''


'''
THIS IS BEN's!
from watson_developer_cloud import AlchemyLanguageV1

url = "https://gateway-a.watsonplatform.net/calls"
api_key = "b8db92daa6a6ca79bb61c0938babe873de0ed914"

alchemy_language = AlchemyLanguageV1(api_key="b8db92daa6a6ca79bb61c0938babe873de0ed914")
'''

'''

  ####  tech_admin@monitor-360.com
{
  "url": "https://gateway-a.watsonplatform.net/calls",
  "note": "It may take up to 5 minutes for this key to become active",
  "apikey": "e581d5843a8e54af4a0b04ab2619cccde2dae747"
}


    # HANNAH ACCOUNT!!
{
  "url": "https://gateway-a.watsonplatform.net/calls",
  "apikey": "d764df8cc016116fe8d2559e52a7474dab6103d4",
  "note": "It may take up to 5 minutes for this key to become active"
}

'''
