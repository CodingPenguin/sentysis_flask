import json
from ytcomment import YTComment
from helpers.analysis import calc_sentiment, find_quartiles

with open('./comment_data.json') as f:
    comment_data = json.load(f)

comment_list = []


def sanitize(data):
    sanitized_data = YTComment(comment_data)
    return sanitized_data

if "items" in comment_data:
    for comment in comment_data["items"]:
        comment_list.append(sanitize(comment))

print([c.sentiment for c in comment_list])

# for i in range(1, len(comment_list)):
#         key = comment_list[i]
#         prev_index = i-1
#         while prev_index >= 0 and key.sentiment < comment_list[prev_index].sentiment :
#                 comment_list[prev_index + 1] = comment_list[prev_index]
#                 prev_index -= 1
#         comment_list[prev_index + 1] = key
#
# print(find_quartiles([c.sentiment for c in comment_list]))

#print([c.value for c in comment_list])

# print(list(comment_list))
