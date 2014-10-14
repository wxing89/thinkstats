import erf
import Cdf
import cumulative
import math
import myplot
import random
import rankit
import thinkstats
import matplotlib.pyplot as pyplot

def ExpoCdf(x, lam):
    '''Evaluates CDF of the exponential distribution with parameter lam.'''
    return 1 - math.exp(-lam * x)

def ParetoCdf(x, alpha, xmin):
    '''Evaluates CDF of the Pareto distribution with parameters alpha, xmin.'''
    if x < xmin:
        return 0
    return 1 - pow(x / xmin, -alpha)

