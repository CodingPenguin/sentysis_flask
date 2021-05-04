import json
from models.ytcomment import YTComment
from helpers.get_sentiment import get_sentiment
from helpers.get_response import get_response
from helpers.get_title import get_title

with open('./comment_data.json') as c:
    comment_data = json.load(c)

with open('./video_data.json') as v:
    video_data = json.load(v)

comments_list = []

for c in comment_data["items"]:
    comment = YTComment(c)
    comments_list.append(comment)

comments_list.sort(key=lambda c: c.sentiment, reverse=True)

title = get_title(video_data)

response = get_response(title, comments_list)
print(response)
print(get_sentiment("Good"))
