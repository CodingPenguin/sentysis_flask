# Sentysis (backend)
This repository is the Flask server that the frontend of this app is built on. This server communicates with the frontend by serving as an API endpoint; furthermore, this server communicates with the YouTube Data API (v3) to retrieve a video's comment data, which will be analyzed through sentiment analysis (using vaderSentiment), and this data will be passed to the frontend API endpoint to be pushed to the user interface. 
<br />Hosted on Heroku.

