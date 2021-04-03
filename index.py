from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import config, googleapiclient.discovery, json, os

from comments import get_comments
from ytcomment import YTComment
from helpers.get_sentiment import get_sentiment
from helpers.get_weighted_stats import get_weighted_stats



app = Flask(__name__)
CORS(app)

comment_list = []

@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>loser</h1>"

@app.route('/api/ytVideoIds', methods=['POST'])
def process_video_id():

    if not request.json or not 'videoId' in request.json:
        abort(400)

    yt_video_id = request.get_json('videoId')
    comment_data = get_comments(yt_video_id) # from line 12, it gets "Bh_uMYaykyQ"

    sentiments = [] # List of each comments' sentiments
    likes = [] # List of likes per comment
    comments = [] # List of text value per comment

    for c in comment_data["items"]:
        comment = YTComment(c)
        sentiments.append(comment.sentiment)
        likes.append(comment.likes)
        comments.append(comment.value)

    weighted_stats = get_weighted_stats(sentiments, likes) # Weighted mean and weighted standard deviation

    return jsonify({'yt_video_id': yt_video_id}), 201



if __name__ == '__main__':
    app.run(debug=True)
