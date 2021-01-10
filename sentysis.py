from flask import Flask, jsonify, request, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

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

@app.route('/api/ytVideoIds', methods=['GET', 'POST'])
def create_ytVideoId():
    if request.method == 'POST':
        if not request.json or not 'videoId' in request.json:
            abort(400)

        ytVideoId = {
            request.get_json('videoId')
        }
        ytVideoIds.append(ytVideoId)
        return jsonify({ytVideoId}), 201
    return jsonify(ytVideoIds)




if __name__ == '__main__':
    app.run(debug=True)
