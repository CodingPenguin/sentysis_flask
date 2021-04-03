from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

afinn = Afinn(language="en")
analysis = SentimentIntensityAnalyzer().polarity_scores

def get_afinn_score(c):
    word_count = len(c.split())
    score = ((afinn.score(c) / word_count) / 5)
    return score

def get_sentiment(c):
    vader_sentiment = analysis(c)["pos"] - analysis(c)["neg"]
    afinn_sentiment = get_afinn_score(c)
    return round(((vader_sentiment + afinn_sentiment) / 2), 3)
