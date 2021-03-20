from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import googleapiclient.discovery, os, config, comments

app = Flask(__name__)
CORS(app)

yt_video_ids= [
    # should look like this
    # {
    #     "videoId":"Bh_uMYaykyQ"
    # }
]

# importing methods basically
get_comments = comments.get_comments


@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>loser</h1>"

@app.route('/api/ytVideoIds', methods=['GET', 'POST'])
def create_ytVideoId():
    if request.method == 'POST':
        if not request.json or not 'videoId' in request.json:
            abort(400)

        yt_video_id = request.get_json('videoId')

        yt_video_ids.append(yt_video_id)
        comment_data = get_comments(yt_video_ids[0]["videoId"]) # from line 12, it gets "Bh_uMYaykyQ"

        return jsonify({'ytVideoId': yt_video_id}), 201
    return jsonify(yt_video_ids)



if __name__ == '__main__':
    app.run(debug=True)
