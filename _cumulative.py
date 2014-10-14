import first
import descriptive
import math
import Cdf
import Pmf
import survey
import thinkstats

import matplotlib.pyplot as pyplot
import myplot


def Process(table, name):
    '''Runs various analyses on this table.

    Creates instance variables:
        weights: sequence of int total weights in ounces
        weight_pmf: Pmf object
        weight_cdf: Cdf object
        oz_pmf: Pmf of just the ounce field
    '''
    descriptive.Process(table, name)

    table.weigths = [p.totalwgt_oz for p in table.records
                     if p.totalwgt_oz != 'NA']

    table.weight_pmf = Pmf.MakePmfFromList(table.weights, table.name)
    table.weight_cdf = Cdf.MakeCdfFromList(table.weights, table.name)


def MakeTables(data_dir='.'):
    '''Reads survey data and returns a tuple of Tables'''
    table, first, others = first.MakeTables(data_dir)
    pool = descriptive.PoolRecords(firsts, others)

    Process(pool, 'live births')
    Process(firsts, 'first babies')
    Process(others, 'others')

    return pool, firsts, others


def Resample(cdf, n=10000):
    sample = cdf.Sample(n)
    new_cdf = Cdf.MakeCdfFromList(sample, 'resampled')
    myplot.Clf()
    myplot.Cdfs([cdf, new_cdf])
    myplot.Save(root='resample_cdf',
                title='CDF',
                xlabel='weight in oz',
                ylabel='CDF(x)')


def MakeExample():
    '''Make a simple example CDF.'''
    t = [2, 1, 3, 2, 5]
    cdf = Cdf.MakeCdfFromList(t)
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='example_cdf',
                title='CDF',
                xlabel='x',
                ylabel='CDF(x)',
                axis=[0, 6, 0, 1],
                legend=False)