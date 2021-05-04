sentiment_emoji = {
    -1.0: "🤬",
    -0.8: "😡",
    -0.6: "😠",
    -0.4: "😒",
    -0.2: "😕",
    0.0: "😐",
    0.2: "🙂",
    0.4: "😀",
    0.6: "😁",
    0.8: "😄",
    1.0: "😆",
}

def get_emoji(n):
    if n in sentiment_emoji:
        return sentiment_emoji[n]
    if round_to_nearest_fifth(n) in sentiment_emoji:
        return sentiment_emoji[round_to_nearest_fifth(n)]

def round_to_nearest_fifth(n):
    return round(n*5)/5
