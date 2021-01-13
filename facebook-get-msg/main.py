from facebook_scraper import get_posts
import json
import datetime


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def get_text(posts):
    for post in posts:
        yield post['post_text']


posts = get_posts("NaftaliBennett", pages=1)
l = list(get_text(posts))
dumps = json.dumps(l, indent=4, cls=Encoder, ensure_ascii=False)
print(dumps)
