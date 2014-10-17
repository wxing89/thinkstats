'''Exercise 4.14

Write a function named weibullvariate that takes lam and 
k and returns a random value from the Weibull distribution 
with those pa- rameters.
'''


import random

import math


def weibullvariate(lam, k):
    p = random.random()
    x = lam * math.pow(-math.log(1-p), 1/k)
    return x