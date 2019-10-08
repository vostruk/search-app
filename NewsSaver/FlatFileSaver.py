# -*- coding: utf-8 -*-
import uuid
import json
import os
from datetime import datetime

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)

class FlatFileSaver:
    root_dir = "saved_articles/"
    def save_article(self, article_dict):
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
        file_name = os.path.join(self.root_dir, article_dict.get("meta").get("publish_date", datetime.now).strftime("%m-%d-%Y") + str(uuid.uuid1()) + ".json")
        with open(file_name, 'w') as outfile:
            json.dump(article_dict, outfile, cls=DatetimeEncoder)