import json
from ytcomment import YTComment
from helpers.analysis import calc_sentiment, find_quartiles

with open('./comment_data.json') as f:
    comment_data = json.load(f)

comment_list = []

for c in comment_data["items"]:
    comment = YTComment(c)
    comment_list.append(comment)

comment_list.sort(key=lambda c: c.sentiment)

print([c.sentiment for c in comment_list])

quartiles = find_quartiles([c.sentiment for c in comment_list])
print(quartiles)
