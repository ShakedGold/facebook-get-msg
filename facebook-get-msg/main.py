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
    user = input("Enter link to groups, users or pages: ")
    fields = user.split("/")
    if fields[2] == "www.facebook.com":
        end_trigger = int(input("Enter the number of posts you want to display: "))
        if fields[3] == "groups":
            for post in list(get_posts(pages=2, group=fields[4]))[:end_trigger]:
                get = post.get("post_text")
                image_get = post.get("image")
                if post["image"] is not None:
                    short = Shortener().tinyurl.short(image_get)
                    print(f'\nPost Text: {get}\nImage: {short}')
                else:
                    print("\nPost Text:", get, "\nImage:", image_get)
            print("...")
        else:
            for post in list(get_posts(fields[3], pages=2))[:end_trigger]:
                get = post.get("post_text")
                image_get = post.get("image")
                if post["image"] is not None:
                    short = Shortener().tinyurl.short(image_get)
                    print(f'\nPost Text: {get}\nImage: {short}\n')
                else:
                    print("\nPost Text:", get, "\nImage:", image_get, "\n")
            print("For more posts:", user)
    else:
        print("not a valid facebook link\n")
        post_text_image()


post_text_image()
