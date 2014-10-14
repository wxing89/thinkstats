'''Exercise 4.8 
Plot the CDF of pregnancy lengths for all live births. 
Does it look like a normal distribution?

Compute the mean and standard deviation of the sample 
and plot the normal distribution with the same parameters. 
Is the normal distribution a good model for this data?
If you had to summarize this distribution with two statistics, 
what statistics would you choose?
'''

import random
import math
import numpy
from scipy.special import erf

import survey
import thinkstats
import Cdf
import myplot


root2 = math.sqrt(2.0)

def main():
    table = survey.Pregnancies()
    table.ReadRecords('.')

    prglengths = [p.prglength for p in table.records if p.prglength != 'NA']

    cdf = Cdf.MakeCdfFromList(prglengths, 'pregnancy lengths CDF')
    
    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear')
    myplot.Save(root='pregnancy_lengths_cdf',
                title='CDF of pregnancy lengths',
                xlabel='weeks',
                ylabel='probability')

    mu, sigma = thinkstats.MeanVar(prglengths)
    normalprg = [random.normalvariate(mu, sigma) for i in range(100)]

    cdf = Cdf.MakeCdfFromList(normalprg, 'normal pregnancy lengths CDF')
    myplot.Cdf(cdf, complement=False, xscale='linear', yscale='linear')
    myplot.Save(root='normal_pregnancy_lengths_cdf',
                title='normal CDF of pregnancy lengths',
                xlabel='weeks',
                ylabel='probability')


if __name__ == '__main__':
    main()
