#
# Exercise 4.1 
#
# For small values of n, we don't expect an empirical distribution
# to fit a continuous distribution exactly. One way to evaluate the quality of
# fit is to generate a sample from a continuous distribution and see how well
# it matches the data.
#
# The function expovariate in the random module generates random values
# from an exponential distribution with a given value of l. Use it to generate
# 44 values from an exponential distribution with mean 32.6. Plot the CCDF
# on a log-y scale and compare it to Figure 4.3.
#
# Hint: You can use the function pyplot.yscale to plot the y axis on a log
# scale.
#
# Or, if you use myplot, the Cdf function takes a boolean option, complement,
# that determines whether to plot the CDF or CCDF, and string options,
# xscale and yscale, that transform the axes; to plot a CCDF on a log-y scale:
# myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log')

import random

import Pmf
import Cdf
import myplot

def main():
    num_lsit = [random.expovariate(1/32.6) for i in range(44)]

    cdf = Cdf.MakeCdfFromList(num_lsit, 'exponential distribution cdf');

    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='exponential_distribution_cdf',
                title='CDF of exponential distribution',
                xlabel='number',
                ylabel='probability')

    myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log');
    myplot.Save(root='exponential_distribution_ccdf',
                title='CCDF of exponential distribution',
                xlabel='number',
                ylabel='probability',
                xscale='linear',
                yscale='log')


if __name__ == '__main__':
    main()