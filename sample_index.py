import json
from ytcomment import YTComment
from helpers.get_sentiment import get_sentiment
from helpers.get_weighted_stats import get_weighted_stats

with open('./comment_data.json') as f:
    comment_data = json.load(f)

sentiments = [] # List of each comments' sentiments
likes = [] # List of likes per comment
comments = [] # List of text value per comment

for c in comment_data["items"]:
    comment = YTComment(c)
    sentiments.append(comment.sentiment)
    likes.append(comment.likes)
    comments.append(comment.value)

weighted_stats = get_weighted_stats(sentiments, likes) # Weighted mean and weighted standard deviation
