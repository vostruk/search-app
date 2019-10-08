from .AbstractUrlProvider import AbstractUrlProvider

class KnownUrlProvider(AbstractUrlProvider):
    _sources = ["https://www.firstpost.com/tech", 
    "https://www.newscientist.com/subject/technology/",
    "https://www.nytimes.com/section/technology",
    "https://www.bbc.com/news/technology",
    "https://www.livescience.com/technology",
    "https://www.sciencedaily.com/news/matter_energy/technology/",
    "https://www.cnet.com/news/",
    "https://edition.cnn.com/business/tech",
    "https://www.theverge.com/tech",
    "https://www.futurity.org/category/science-technology/",
    "https://scitechdaily.com/",
    "https://www.technewsworld.com/"]
    
    """
    method returns generator of urls of websites with specific topic
    """
    def get_news_source(self, topic):
        for source in self._sources:
            yield source