from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import googleapiclient.discovery, os, config
from comments import get_comments


app = Flask(__name__)
CORS(app)

comment_list = []

@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>loser</h1>"

@app.route('/api/ytVideoIds', methods=['POST'])
def create_ytVideoId():

    if not request.json or not 'videoId' in request.json:
        abort(400)

    yt_video_id = request.get_json('videoId')
    comment_data = get_comments(yt_video_id) # from line 12, it gets "Bh_uMYaykyQ"

    return jsonify({'ytVideoId': yt_video_id}), 201

def sanitize(data):
    sanitized_data = YTComment(data)
    return sanitized_data

for comment in comment_data["items"]:
    comment_list.append(sanitize(comment))

comment_list = sort(comment_list)

print([c.sentiment for c in comment_list])

quartiles = find_quartiles([c.sentiment for c in comment_list])
print(quartiles)

if __name__ == '__main__':
    app.run(debug=True)
