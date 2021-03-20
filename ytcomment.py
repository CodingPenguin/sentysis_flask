from helpers.analysis import calc_sentiment
class YTComment:
    def __init__(self, data):
        self.value = ""
        self.likes = 0
        self.sentiment = 0
        #
        if "snippet" in data:
            if "topLevelComment" in data["snippet"]:
                if "snippet" in data["snippet"]["topLevelComment"]:
                    real_data = data["snippet"]["topLevelComment"]["snippet"]
                    if "textDisplay" in real_data:
                        self.value = real_data["textDisplay"]
                    if "likeCount" in real_data:
                        self.likes = real_data["likeCount"]

        self.sentiment = calc_sentiment(self.value)

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
