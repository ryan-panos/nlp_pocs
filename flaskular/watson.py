import json
from watson_developer_cloud import AlchemyLanguageV1


class MonitorWatsonAPI():
    API_KEY = "e581d5843a8e54af4a0b04ab2619cccde2dae747"
    OLD_RP_API_KEY = "c4eee5a628ea2243350787a04b924bb21ecb6f7e"
    BEN_API_KEY = "b8db92daa6a6ca79bb61c0938babe873de0ed914"
    DO_NOT_CALL = False

    def __init__(self):
        self.alchemy_handle = AlchemyLanguageV1(api_key=MonitorWatsonAPI.API_KEY)

    def give_all_nlp(self, content_txt):
        return_data={
            "orginal_text":content_txt
        }

        sent = self.get_ibm_sentiment(content_txt)
        # Check for error?
        if sent is not None:
            return_data['sentiment'] = sent

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

        return return_data


    def get_ibm_sentiment(self, txt_str):
      if self.DO_NOT_CALL == True:
          return "POS"

      alchemy_language = AlchemyLanguageV1(api_key=MonitorWatsonAPI.API_KEY)
      sent_resp = alchemy_language.sentiment(text=txt_str)
      print(json.dumps(
          sent_resp,
        indent=2))  # indent??

      print " >>> CALLED IBM - sent_resp: " + str(sent_resp)
      return sent_resp


    # def get_ibm_sentiment(txt_str):
    #   if DO_NOT_CALL == True:
    #       return "Phil"
    #
    #   alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
    #   print(json.dumps(
    #       alchemy_language.entities(
    #           text=txt_str),
    #       indent=2))  # indent??
    #
    #   return alchemy_language.entities(text=txt_str)





'''

Services available - Per IBM Rep (Jacob Ellison <jellison@us.ibm.com>):

    Emotion & Sentiment analysis - Both are available as Watson APIs under the AlchemyLanguage Service
    Sentence/Document Level Sentiment/Emotion (DLS/E) - Both are available as Watson APIs under the AlchemyLanguage Service
    Entity Level Sentiment/Emotion (ELS/E) - Both are available as Watson APIs under the AlchemyLanguage service
    Relation Extraction (RelEx) - Available as a Watson API under the AlchemyLanguage service
    Named Entity Recognition (NER) - Available as a Watson API under the AlchemyLanguage service
    Named Entity Disambiguation (NED) - Included in the results of NER API Calls.
    Topic Extraction (TopEx) - Taxonomy, Concept Tagging and Keyword Extraction with relevance scores, all available under the AlchemyLanguage service are probably the closest proxy to Topic Extraction.

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
'''
