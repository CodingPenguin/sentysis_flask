import json

with open('./comment_data.json') as f:
    comment_data = json.load(f)

comment_list = []

if "items" in comment_data:
    comment_data_items = comment_data["items"]
    for comment in comment_data_items:
        if "snippet" not in comment:
            break
        comment_snippet = comment["snippet"]
        if "topLevelComment" not in comment_snippet:
            break
        comment_top_level_comment = comment_snippet["topLevelComment"]
        if "snippet" not in comment_top_level_comment:
            break
        comment_snippet_1 = comment_top_level_comment["snippet"]
        if "textDisplay" not in comment_snippet_1:
            break
        comment_text_display = comment_snippet_1["textDisplay"]
        comment_list.append(comment_text_display)
else:
    ""

# for comment in comment_list:
#     print(comment + "\n")
