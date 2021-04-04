from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import config, googleapiclient.discovery, json, os

from helpers.fetch_comments import fetch_comments
from models.ytcomment import YTComment
from helpers.get_response import get_response


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
    # comment_data = fetch_comments(yt_video_id) # from line 12, it gets "Bh_uMYaykyQ"
    # video_title = fetch_title(yt_video_id)
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

    return jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=True)
