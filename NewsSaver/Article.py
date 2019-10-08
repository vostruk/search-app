from data_object import DataObject


class Article(DataObject):

    def __init__(self, topic, title, author, date, text, image_url):
        self.title = title
        self.author = author
        self.date = date
        self.text = text
        self.image_url = image_url
        self.topic = topic

    @property
    def topic(self):
        return self.topic