from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import config, googleapiclient.discovery, json, os

from comments import get_comments
from ytcomment import YTComment
from helpers.analysis import calc_sentiment, find_quartiles



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

    for c in comment_data["items"]:
        comment = YTComment(c)
        comment_list.append(comment)

    comment_list.sort(key=lambda c: c.sentiment)

    quartiles = find_quartiles([c.sentiment for c in comment_list])

    return jsonify({'yt_video_id': yt_video_id}), 201



if __name__ == '__main__':
    app.run(debug=True)
