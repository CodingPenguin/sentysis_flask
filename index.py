from flask import Flask, jsonify, request, abort
from flask_cors import CORS

from helpers.fetch_comments import fetch_comments
from models.ytcomment import YTComment
from helpers.get_response import get_response


app = Flask(__name__)
CORS(app)

comment_list = []

@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>what's up</h1>"

@app.route('/api/ytVideoId', methods=['POST'])
def process_video_id():
    if not request.json or "videoId" not in request.json:
        abort(400)

    yt_video_id = request.get_json('videoId')['videoId']
    comment_data = fetch_comments(yt_video_id)

    comments_list = sorted([YTComment(c) for c in comment_data["items"]], key=lambda c: c.sentiment, reverse=True)

    response = get_response(comments_list)

    return jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=True)
