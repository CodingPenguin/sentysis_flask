from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy

afinn = Afinn(language="en")
analysis = SentimentIntensityAnalyzer().polarity_scores

def calc_sentiment(c):
    vader_sentiment = analysis(c)["pos"] - analysis(c)["neg"]
    return vader_sentiment


#uncomment the following 2 methods if I want to normalize data
# def word_count(text_string):
#     # '''Calculate the number of words in a string'''
#     return len(text_string.split())

# def normalize_data(sentiment_score, sentiment_data): # https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc
#     normalized_score = (2 * ((sentiment_score - numpy.min(sentiment_data)) / (numpy.max(sentiment_data) - numpy.min(sentiment_data)))) - 1
#     return normalized_score # sentiment between -1 and 1

# sentiment_list = list(map(calc_sentiment, comment_value_list))


# TODO: split this in half or something and then implement the above thing boi put this up commentThreadListResponse?

# sort sentiment_list

def find_quartiles(list):
    first_quartile = round(numpy.percentile(list, 25, interpolation = 'midpoint'), 3)
    third_quartile = round(numpy.percentile(list, 75, interpolation = 'midpoint'), 3)
    print(list)
    avg_sentiment = round(numpy.median(list), 3)
    output = "The median sentiment is " + str(avg_sentiment) + " with the middle 50% of the sentiment varying from " + str(first_quartile) + " to " + str(third_quartile) + "."
    return output
