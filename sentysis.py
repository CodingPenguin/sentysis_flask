from flask import Flask, jsonify, request

sentysis = Flask(__name__)

links = [
    {
    # should look like this
    # "link": {
    #   "youtube_url": "https://www.youtube.com/watch\?v\=1ecG3MT0lAw"
    #   }
    }
]

@sentysis.route('/')
def create_UI():
    return "<h1>WHAT'S UP LOSER</h1>"

@sentysis.route('/api/v1.0/links', methods=['GET', 'POST'])
def create_youtube_url():

if request.method == 'POST':
    if not request.json or not 'youtube_url' in request.json:
        abort(400)
    link = {
        'youtube_url': request.json['youtube_url']
    }
    links.append(link)
    return jsonify({'link': link}), 201



if __name__ == '__main__':
    sentysis.run(debug=True)
