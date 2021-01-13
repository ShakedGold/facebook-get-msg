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
if user.split("/")[2] == "www.facebook.com":
    for post in get_posts(field, pages=1):
        print("Post Text:", post["post_text"], "\n", "Image:", post["image"], "\n")
else:
    print("not a valid facebook link")

# json.dumps(post, ensure_ascii=False, cls=Encoder, indent=4)
