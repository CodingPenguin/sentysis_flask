from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ytUrls = [
    {
    # should look like this
    # "ytUrl": {
    #   "youtube_url": "https://www.youtube.com/watch\?v\=1ecG3MT0lAw"
    #   }
    }
]



@app.route('/')
def create_UI():
    return "<h1>WHAT'S UP LOSER</h1>"

@app.route('/api/ytUrls', methods=['GET', 'POST'])
@cross_origin()
def create_youtube_url():


    if request.method == 'POST':
        if not request.json or not 'youtube_url' in request.json:
            abort(400)
            ytUrl = {
            'youtube_url': request.json['youtube_url']
            }
            ytUrls.append(ytUrl)
            return jsonify({'ytUrl': ytUrl}), 201
    else: # 'GET' http method
        return ytUrls[0], 201



#if __name__ == '__main__':
#    app.run(debug=True)
