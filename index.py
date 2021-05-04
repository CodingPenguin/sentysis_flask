from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import config, googleapiclient.discovery, json, os

from helpers.fetch_comments import fetch_comments
from helpers.fetch_title import fetch_title
from models.ytcomment import YTComment
from helpers.get_response import get_response
from helpers.get_title import get_title


app = Flask(__name__)
CORS(app)

comment_list = []

@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>what's up</h1>"

@app.route('/api/ytVideoIds', methods=['POST'])
def process_video_id():

    if not request.json or "videoId" not in request.json:
        abort(400)

    yt_video_id = request.get_json('videoId')

    # comment_data = fetch_comments(yt_video_id) # from line 12, it gets "Bh_uMYaykyQ"
    # video_title = fetch_title(yt_video_id)
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

    return jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=True)
