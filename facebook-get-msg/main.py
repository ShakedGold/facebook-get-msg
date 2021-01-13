from facebook_scraper import get_posts
from pyshorteners import Shortener
import json
import datetime


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def post_text_image():
    user = input("Enter link to page or user: ")
    field = user.split("/")[3]
    if user.split("/")[2] == "www.facebook.com":
        for post in get_posts(field, pages=1):
            get = post.get("post_text")
            post_get = post.get("image")
            if post["image"] is not None:
                short = Shortener().tinyurl.short(post_get)
                print(f'Post Text: {get}\n\nImage: {short}\n')
            else:
                print("Post Text:", get, "\n\nImage:", post_get, "\n")
    else:
        print("not a valid facebook link\n")
        post_text_image()


post_text_image()
# json.dumps(post, ensure_ascii=False, cls=Encoder, indent=4)
