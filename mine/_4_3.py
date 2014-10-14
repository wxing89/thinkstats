#
# Exercise 4.3 
# The random module provides paretovariate, which generates
# random values from a Pareto distribution. It takes a parameter for a, but
# not xm. The default value for xm is 1; you can generate a distribution with a
# different parameter by multiplying by xm.
#
# Write a wrapper function named paretovariate that takes a and xm as pa-
# rameters and uses random.paretovariate to generate values from a two-
# parameter Pareto distribution.
#
# Use your function to generate a sample from a Pareto distribution. Com-
# pute the CCDF and plot it on a log-log scale. Is it a straight line? What is
# the slope?

import random

import Cdf
import myplot

# alpha = 1
# xm = 0.5
def main():
    alpha = 1
    xm = 0.5
    num_list = [ xm * random.paretovariate(alpha) for i in range(1000) ]

    cdf = Cdf.MakeCdfFromList(num_list, 'pareto distribution cdf');

    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='pareto_distribution_cdf',
                title='CDF of pareto distribution',
                xlabel='number',
                ylabel='probability')

    cdf = Cdf.MakeCdfFromList(num_list, 'pareto distribution ccdf');
    myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log');
    myplot.Save(root='pareto_distribution_ccdf',
                title='CCDF of pareto distribution',
                xlabel='number',
                ylabel='probability',
                xscale='log',
                yscale='log')


if __name__ == '__main__':
    main()
