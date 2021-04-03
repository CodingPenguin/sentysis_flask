import numpy, math

def get_weighted_stats(sentiments, likes):
    weighted_mean = round(numpy.average(sentiments, weights=likes), 3)
    weighted_std = round(math.sqrt(numpy.average((sentiments-weighted_mean)**2, weights=likes)), 3)
    return {
        "weighted_mean": weighted_mean,
        "weighted_std": weighted_std
    }
