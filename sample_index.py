import json
from ytcomment import YTComment
from helpers.analysis import calc_sentiment, find_quartiles
from helpers.sentiment_sort import sort

with open('./comment_data.json') as f:
    comment_data = json.load(f)

comment_list = []


def sanitize(data):
    sanitized_data = YTComment(data)
    return sanitized_data

for comment in comment_data["items"]:
    comment_list.append(sanitize(comment))

comment_list = sort(comment_list)

print([c.sentiment for c in comment_list])

quartiles = find_quartiles([c.sentiment for c in comment_list])
print(quartiles)
