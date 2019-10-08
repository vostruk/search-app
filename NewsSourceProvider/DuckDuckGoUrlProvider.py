from .AbstractUrlProvider import AbstractUrlProvider
import urllib.parse
import requests
from bs4 import BeautifulSoup

class DuckDuckGoUrlProvider(AbstractUrlProvider):
    
    _duck_duck_url = "https://duckduckgo.com/html/?q="

    """
    method returns generator of urls of websites with specific topic
    """
    def get_news_source(self, topic="Iphone"):
        query = "technology news"
        quoted_query = urllib.parse.quote(query)
        r = requests.get(self._duck_duck_url + quoted_query)
        yield r.text
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all('a', attrs={'class':'result__a'}, href=True)
        for link in results:
            url = link['href']
            o = urllib.parse.urlparse(url)
            d = urllib.parse.parse_qs(o.query)
            yield d['uddg'][0]
