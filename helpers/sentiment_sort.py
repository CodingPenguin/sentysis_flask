def sort(comment_list):
    for i in range(1, len(comment_list)):
        key = comment_list[i]
        prev_index = i-1
        while prev_index >= 0 and key.sentiment < comment_list[prev_index].sentiment :
                comment_list[prev_index + 1] = comment_list[prev_index]
                prev_index -= 1
        comment_list[prev_index + 1] = key

    return comment_list
