from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)

ytVideoIds= [
    {
    # should look like this
    # "ytVideoId": {
    #   "videoId": "1ecG3MT0lAw"
    #   }
    }
]



@app.route('/')
def create_UI():
    return "<h1>WHAT'S UP LOSER</h1>"

@app.route('/api/ytVideoIds', methods=['POST'])
def create_ytVideoId():

    if not request.json or not 'videoId' in request.json:
            abort(400)

    ytVideoId = {
        'videoId': request.json['videoId']
    }
    ytVideoIds.append(ytVideoId)
    return jsonify({'ytVideoId': ytVideoId}), 201




if __name__ == '__main__':
    app.run(debug=True)
