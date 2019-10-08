from bs4 import BeautifulSoup, SoupStrainer
import requests
from NewsSourceProvider import AbstractUrlProvider

class SimpleNewsScraper:

    def __init__(self, abstractUrlProvider):
        self.url_provider = abstractUrlProvider

    def get_urls_from_page(self, url):
        page = requests.get(url)    
        data = page.text
        soup = BeautifulSoup(data)

        for link in soup.find_all('a'):
            yield link.get('href')

    def get_text_from_url(self, url):
        res = requests.get(url)
        html_page = res.content 
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style'
        ]
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        return output