# 
# Exercise 4.6 
# The Weibull distribution is a generalization of the exponential
# distribution that comes up in failure analysis (see 
# http://wikipedia.org/wiki/Weibull_distribution).
# 
# Its CDF is
# CDF(x) = 1 - exp(-(x / k)**lambda)
#
# Can you find a transformation that makes a Weibull distribution look like 
# a straight line? What do the slope and intercept of the line indicate?
#
# Use random.weibullvariate to generate a sample from a Weibull distribution
# and use it to test your transformation.



import random

import Pmf
import Cdf
import math
import myplot
import matplotlib.pyplot as plt

# lambda: scale parameter, user alpha
# k: shape parameter, use beta
def main():
    alpha = 1
    beta = 5
    num_list = [ random.weibullvariate(alpha, beta) for i in range(8) ]

    cdf = Cdf.MakeCdfFromList(num_list, 'weibull distribution cdf');

    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='weibull_distribution_cdf',
                title='CDF of weibull distribution',
                xlabel='number',
                ylabel='probability')
    myplot.Clf()

    c_xs = cdf.xs[:-1]
    c_ps = [ (-math.log(1 - p)) ** (1/beta) for p in cdf.ps if p < 1]
    ccdf = Cdf.Cdf(xs=c_xs, ps=c_ps, name='weibull distribution ccdf');
    plt.plot(c_ps, c_xs)
    plt.show()
    myplot.Cdf(ccdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='weibull_distribution_ccdf',
                title='CCDF of weibull distribution',
                xlabel='number',
                ylabel='probability')


if __name__ == '__main__':
    main()