from textblob import TextBlob, Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import numpy

untrained = Blobber(analyzer=NaiveBayesAnalyzer())

def calc_sentiment(c):
    analysis = untrained(c).sentiment
    sentiment = round(analysis.p_pos - analysis.p_neg, 3) # round to three decimal places. ex: 0.345629 rounds to 0.346
    return sentiment

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
