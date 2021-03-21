from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy

afinn = Afinn(language="en")
analysis = SentimentIntensityAnalyzer().polarity_scores

def calc_sentiment(c):
    vader_sentiment = analysis(c)["pos"] - analysis(c)["neg"]
    afinn_sentiment = afinn_score(c)
    return round(((vader_sentiment + afinn_sentiment) / 2), 3)

def afinn_score(c):
    word_count = len(c.split())
    score = ((afinn.score(c) / word_count) / 5)
    return score


# def normalize_data(sentiment_score, sentiment_data): # https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc
#      normalized_score = (2 * ((sentiment_score - numpy.min(sentiment_data)) / (numpy.max(sentiment_data) - numpy.min(sentiment_data)))) - 1
#      return normalized_score # sentiment between -1 and 1


def find_quartiles(list):
    first_quartile = round(numpy.percentile(list, 25, interpolation = 'midpoint'), 3)
    third_quartile = round(numpy.percentile(list, 75, interpolation = 'midpoint'), 3)
    avg_sentiment = round(numpy.median(list), 3)
    output = "The median sentiment is " + str(avg_sentiment) + " with the middle 50% of the sentiment varying from " + str(first_quartile) + " to " + str(third_quartile) + "."
    return output
