import numpy, math
from helpers.get_weighted_mean import get_weighted_mean

def get_weighted_std_dev(sentiments, likes):
    return round(math.sqrt(numpy.average((sentiments-get_weighted_mean(sentiments, likes))**2, weights=likes)), 3)
