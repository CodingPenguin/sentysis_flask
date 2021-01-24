from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import googleapiclient.discovery, os, config, comments

app = Flask(__name__)
CORS(app)

ytVideoIds= [
    # should look like this
    # {
    #     "videoId":"Bh_uMYaykyQ"
    # }
]

# importing methods basically
getComments = comments.getComments


@app.route('/')
def create_UI():
    return "<h1 style='color:red;'>loser</h1>"

@app.route('/api/ytVideoIds', methods=['GET', 'POST'])
def create_ytVideoId():
    if request.method == 'POST':
        if not request.json or not 'videoId' in request.json:
            abort(400)

        ytVideoId = request.get_json('videoId')

        ytVideoIds.append(ytVideoId)
        commentData = getComments(ytVideoIds[0]["videoId"]) # from line 12, it gets "Bh_uMYaykyQ"

        return jsonify({'ytVideoId': ytVideoId}), 201
    return jsonify(ytVideoIds)










if __name__ == '__main__':
    app.run(debug=True)
