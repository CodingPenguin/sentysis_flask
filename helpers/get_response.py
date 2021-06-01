import json
from helpers.get_weighted_mean import get_weighted_mean
from helpers.get_weighted_std_dev import get_weighted_std_dev
from helpers.get_avg_likes_count import get_avg_likes_count
from flask import jsonify

def get_response(comments_list):
    sentiments = []
    likes = []
    comments = []

    for c in comments_list:
        comments.append(c.__dict__)
        sentiments.append(c.sentiment)
        likes.append(c.likes)

    response = {
        "comments": comments,
        "statistics": {
            "avg_likes_count": get_avg_likes_count(likes),
            "weighted_mean": get_weighted_mean(sentiments, likes),
            "weighted_std_dev": get_weighted_std_dev(sentiments, likes),
        }
    }
    return response
