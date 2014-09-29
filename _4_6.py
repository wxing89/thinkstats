# 
# Exercise 4.6 
# The Weibull distribution is a generalization of the exponential
# distribution that comes up in failure analysis (see 
# http://wikipedia.org/wiki/Weibull_distribution).
# 
# Its CDF is
# CDF(x) = 1 - exp(-(x / k)**lambda)
#
# Can you find a transformation that makes aWeibull distribution look like a
# straight line? What do the slope and intercept of the line indicate?
#
# Use random.weibullvariate to generate a sample from a Weibull distribu-
# tion and use it to test your transformation.



import random

import Pmf
import Cdf
import myplot

# lambda: scale parameter, user alpha
# k: shape parameter, use beta
def main():
    alpha = 1
    beta = 5
    num_list = [ random.weibullvariate(alpha, beta) for i in range(1000) ]

    cdf = Cdf.MakeCdfFromList(num_list, 'weibull distribution cdf');

    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='weibull_distribution_cdf',
                title='CDF of weibull distribution',
                xlabel='number',
                ylabel='probability')

    cdf = Cdf.MakeCdfFromList(num_list, 'weibull distribution ccdf');
    myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log');
    myplot.Save(root='weibull_distribution_ccdf',
                title='CCDF of weibull distribution',
                xlabel='number',
                ylabel='probability',
                xscale='log',
                yscale='log')


if __name__ == '__main__':
    main()