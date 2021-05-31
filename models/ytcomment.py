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


