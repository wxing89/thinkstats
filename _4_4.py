#
# Exercise 4.4 
#
# To get a feel for the Pareto distribution, imagine what the world
# would be like if the distribution of human height were Pareto. Choosing the
# parameters xm = 100 cm and alpha = 1.7, we get a distribution with a reasonable
# minimum, 100 cm, and median, 150 cm.

# Generate 6 billion random values from this distribution. What is the mean
# of this sample? What fraction of the population is shorter than the mean?
# How tall is the tallest person in Pareto World?

import random

import Cdf
import myplot

# alpha = 1.7
# xm = 100
def main():
    alpha = 1.7
    xm = 100

    h_num = 6 * 10000
    h_list = [ xm * random.paretovariate(alpha) for i in range(h_num) ]

    h_mean = float(sum(h_list) / h_num)
    print 'human height mean:', h_mean

    num_shorter = 0
    max_height = 0
    for h in h_list:
        if h < h_mean:
            num_shorter += 1
        if h > max_height:
            max_height = h

    print 'population shorter than mean height:', num_shorter
    print 'tallest person\'s height:', max_height


    cdf = Cdf.MakeCdfFromList(h_list, 'human height distribution cdf');

    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear');
    myplot.Save(root='human_height_distribution_cdf',
                title='CDF of human height distribution',
                xlabel='number',
                ylabel='probability')

    cdf = Cdf.MakeCdfFromList(h_list, 'human height distribution ccdf');
    myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log');
    myplot.Save(root='human_height_distribution_ccdf',
                title='CCDF of human height distribution',
                xlabel='number',
                ylabel='probability',
                xscale='log',
                yscale='log')


if __name__ == '__main__':
    main()