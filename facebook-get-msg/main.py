from facebook_scraper import get_posts
import json
import datetime


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


user = input("Enter link to page or user: ")
field = user.split("/")[3]
for post in get_posts(field, pages=1):
    print("New Post:\n", json.dumps(post, ensure_ascii=False, cls=Encoder, indent=4), "\n")
