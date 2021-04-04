import json
from models.ytcomment import YTComment
from helpers.get_sentiment import get_sentiment
from helpers.get_response import get_response

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

response = get_response(comments, sentiments, likes)
print(response)
