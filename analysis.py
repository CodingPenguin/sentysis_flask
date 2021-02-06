import json

with open('./commentData.json') as f:
    commentData = json.load(f)

commentList = []

if "items" in commentData:
    commentData_items = commentData["items"]
    for comment in commentData_items:
        if "snippet" not in comment:
            break
        comment_snippet0 = comment["snippet"]
        if "topLevelComment" not in comment_snippet0:
            break
        comment_topLevelComment = comment_snippet0["topLevelComment"]
        if "snippet" not in comment_topLevelComment:
            break
        comment_snippet1 = comment_topLevelComment["snippet"]
        if "textDisplay" not in comment_snippet1:
            break
        comment_textDisplay = comment_snippet1["textDisplay"]
        commentList.append(comment_textDisplay)
else:
    ""

for comment in commentList:
    print(comment + "\n")
