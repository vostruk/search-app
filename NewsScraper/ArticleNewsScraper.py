from newspaper import Article
import newspaper

class ArticleNewsScraper:

    def get_urls_from_page(self, url):
        cnn_paper = newspaper.build(url)
        for article in cnn_paper.articles:
            yield article.url

    def get_categories_from_url(self, url):
        cnn_paper = newspaper.build(url)
        for category in cnn_paper.category_urls():
            if "tech" in str(category):
                yield category
    
    """returns json table of article objects"""
    def get_articles_from_url(self, url):
        cnn_paper = newspaper.build(url)
        if len(cnn_paper.articles)<2:
            yield self.get_article_from_url(url)

        for cnn_article in cnn_paper.articles:
            cnn_article.download()
            cnn_article.parse()
            cnn_article.nlp()
            yield self.get_article_obj_from_article(cnn_article)


    def get_article_obj_from_article(self, article):
        article_data = dict()
        article_meta = dict()
        article_meta["authors"] = article.authors
        article_meta["publish_date"] = article.publish_date
        article_data["title"] = article.title
        article_data["text"] = article.text
        article_data["image"] = article.top_image
        article_data["movies"] = article.movies
        article_meta["keywords"] = article.keywords
        article_meta["summary"] =  article.summary
        article_data["meta"] = article_meta
        return article_data

    def get_article_from_url(self, url):
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return self.get_article_obj_from_article(article)

