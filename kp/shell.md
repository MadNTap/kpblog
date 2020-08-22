import json
>>> from blog.models import Post
>>> with open('posts.json') as f:
...     posts_json = json.load(f)w