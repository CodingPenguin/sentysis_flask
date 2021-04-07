from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis = SentimentIntensityAnalyzer().polarity_scores

def get_sentiment(c):
    vader_sentiment = analysis(c)["compound"]
    return round((vader_sentiment), 3)
