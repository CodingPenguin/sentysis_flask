from helpers.get_sentiment import get_sentiment
from helpers.spellcheck import spellcheck
from helpers.get_emoji import get_emoji

class YTComment:
    def __init__(self, data):
        self.value = '' # Comment written by the author
        self.likes = 1 # Start with 1 like to include the author of the comment
        # Decimal scale: Worst(-1.0) < Little Above Average(0.5) < Love(1.0)
        self.sentiment = 0

        if "snippet" not in data:
            return

        if "topLevelComment" not in data["snippet"]:
            return

        if "snippet" not in data["snippet"]["topLevelComment"]:
            return

        snippet = data["snippet"]["topLevelComment"]["snippet"]
        if "textDisplay" not in snippet:
            return

        self.value = spellcheck(snippet["textDisplay"])
        self.sentiment = get_sentiment(self.value)
        self.likes = (snippet["likeCount"] + self.likes) if "likeCount" in snippet else 0
        self.emoji = get_emoji(self.sentiment)


#
# ### backend
#
# # /models/ytube.py
# class Ytube:
#   def __init__(self, data):
#     if snippet in data:
#       self.snippet = data['snippet']
#
#     if id in data:
#       self.id = data['id']
#
#     if value in data:
#       self.value = data['value']
#
# # /helpers/analyses.py
#
# def get_quatile(data):
#   pass
#
# # Python program to demonstrate working
# # of map.
#
# # Return double of n
# def addition(n):
#     return n + n
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))
#
# # index.py
# from models import Ytube
# from helpers.analyses import get_quatile:
#
# def sanitise(data):
#   # 1. Sanitise the data
#   comment = Ytube(comment_raw)
#
#
# def get(payload):
#
#   if videoId not in payload:
#     throw error
#
#   videoId = payload.get('videoId')
#
#   if not videoId:
#     throw error
#
#   response = youtube.call.get(videoId)
#   if results not in response:
#     throw error
#
#   youtube_comments = map(sanitise, response.get('results'))
#
#   quartile = get_quatile(youtube_comments)
#   process1 = process1(youtube_comments)
#   process2 = process2(youtube_comments)
#   process3 = process3(youtube_comments)
#
#   results = {
#     'quatile': {
#       'first': '',
#       'second': '',
#       'third': '',
#       'quater': '',
#     },
#     # so forth
#   }
#
# return results
