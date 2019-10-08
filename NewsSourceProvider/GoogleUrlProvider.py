from .AbstractUrlProvider import AbstractUrlProvider
from googlesearch import search

class GoogleUrlProvider(AbstractUrlProvider):
    
    """
    method returns generator of urls of websites with specific topic
    """
    def get_news_source(self, topic=""):
        query = "technology news " + topic
        return search(query, tld="com", lang='en', num=10, stop=None, pause=2)