import json
from analysis import *

with open('./comment_data.json') as f:
    comment_data = json.load(f)

comment_list = []

class YTComment:
    def __init__(self, value, likes, sentiment):
        self.value = value
        self.likes = likes
        self.sentiment = sentiment

# i parsed outside of the class
if "items" in comment_data:
    comment_data_items = comment_data["items"]
    for comment in comment_data_items:
        # general parse
        if "snippet" not in comment:
            break
        comment_snippet = comment["snippet"]
        if "topLevelComment" not in comment_snippet:
            break
        comment_top_level_comment = comment_snippet["topLevelComment"]
        if "snippet" not in comment_top_level_comment:
            break
        comment_snippet_1 = comment_top_level_comment["snippet"]

        # TEXT_DISPLAY PARSED
        if "textDisplay" not in comment_snippet_1:
            break
        comment_text_display = comment_snippet_1["textDisplay"]
        # LIKE_COUNT PARSED
        if "likeCount" not in comment_snippet_1:
            break
        comment_like_count = comment_snippet_1["likeCount"]

        youtube_comment = YTComment(comment_text_display, comment_like_count, calc_sentiment(comment_text_display))
        comment_list.append(youtube_comment)

for i in range(1, len(comment_list)):
        key = comment_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        prev_index = i-1
        while prev_index >= 0 and key.sentiment < comment_list[prev_index].sentiment :
                comment_list[prev_index + 1] = comment_list[prev_index]
                prev_index -= 1
        comment_list[prev_index + 1] = key

print(find_quartiles([c.sentiment for c in comment_list]))

#print([c.value for c in comment_list])
