import json
import weightedstats as ws
import weightedcalcs as wc
from ytcomment import YTComment
from helpers.analysis import calc_sentiment, weighted_stats

with open('./comment_data.json') as f:
    comment_data = json.load(f)

calc = wc.Calculator("likes")
comment_list = []

for c in comment_data["items"]:
    comment = YTComment(c)
    comment_list.append(comment)

comment_list.sort(key=lambda c: c.sentiment)

sentiment_list = [c.sentiment for c in comment_list]
likes_list = [c.likes for c in comment_list]

weighted_stats = weighted_stats(sentiment_list, likes_list)

print(weighted_stats)
print(sentiment_list)
# print([c.value for c in comment_list])

# weighted_median = ws.numpy_weighted_median(sentiment_list, weights=likes_list)
# print(weighted_median)
# quartiles = find_quartiles([c.sentiment for c in comment_list])
# print(quartiles)
