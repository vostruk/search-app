from flask import Flask
from flask import request
from NewsSourceProvider.GoogleUrlProvider import GoogleUrlProvider
from NewsSourceProvider.DuckDuckGoUrlProvider import DuckDuckGoUrlProvider
from NewsScraper.SimpleNewsScraper import SimpleNewsScraper
from NewsSaver.FlatFileSaver import FlatFileSaver
from NewsScraper.ArticleNewsScraper import ArticleNewsScraper
app = Flask(__name__)

gs = GoogleUrlProvider()
ddg = DuckDuckGoUrlProvider()
sns = SimpleNewsScraper(GoogleUrlProvider)

flatFileSaver = FlatFileSaver()
articleNewsScraper = ArticleNewsScraper()

@app.route('/')
def hello():
    return "hello world. Search for articles with /search?t=topic&n=articles endpoint"

@app.route('/search')
def search():
    topic = request.args.get('t')
    number = int(request.args.get('n'))

    count = 0
    count_all = 0
    for source in gs.get_news_source(topic):
        count+=1
        print("Google " + source, flush=True)
        for category in articleNewsScraper.get_categories_from_url(source):
            print("Category: " + category, flush=True)
            for article in articleNewsScraper.get_articles_from_url(category):
                print("Art: " + article.get("title"), flush=True)
                flatFileSaver.save_article(article)
                count_all+=1
        if count>number:
            break
    return str("Downloaded " + str(count_all) + " articles")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


