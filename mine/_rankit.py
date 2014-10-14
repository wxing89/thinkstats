import random
import thinkstats
import myplot
import matplotlib.pyplot as pyplot

def Sample(n=6):
    '''Generates a smaple from a standard normal vairate.

    n: sample size

    Returns: list of n floats
    '''
    t = [random.normalvariate(0.0, 1.0) for i in range(n)]
    t.sort()
    return t


def Samples(n=6, m=1000):
    '''Generates m samples with size n each.

    n: sample size
    m: number of samples

    Returns: list of samples
    '''
    t = [Samples(n) for i in range(m)]
    return t


def EstimateRankits(n=6, m=1000):
    '''Estimate the expected values of sorted random samples.

    n: sample size
    m: number of iterations

    Returns: list of n rankits
    '''
    t = Samples(n, m)
    t = zip(*t)
    means = [thinkstats.Mean(x) for x in t]
    return means


def MakeNormalPlot(ys, root=None, line_options={}, **options):
    '''Make a normal probability plot.

    Args:
        ys: sequence of values
        line_options: dictionary of options for pyplot.plot
        options: dictionary of options for myplot.save
    '''
    # TODO: when n is samll, generate a larger sample and desample
    n = len(ys)
    xs = [random.normalvariate(0.0, 1.0) for i in range(n)]

    pyplot.clf()
    pyplot.plot(sorted(xs), sorted(ys), 'b.', markersize=3, **line_options)

    myplot.Save(root,
                xlabel='Standard normal values',
                legend=False,
                **options)


def main():
    l = [ random.normalvariate(0, 1) for i in range(100)]
    MakeNormalPlot(l, root='range_100')


if __name__ == "__main__":
    main()