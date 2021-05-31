import numpy, math

def get_weighted_mean(sentiments, likes):
    return round(numpy.average(sentiments, weights=likes), 3)
