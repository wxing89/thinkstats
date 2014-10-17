import Cdf
import math
import myplot
import populations
import rankit
import thinkstats


def MakeFigures():
    pops = populations.ReadData()
    print len(pops)

    cdf = Cdf.MakeCdfFromList(pops, 'populations')
    myplot.Cdf(cdf)
    myplot.Save(root='populations',
                title='City/Town Populations',
                xlabel='populations',
                ylabel='CDF',
                legend=False)

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='populations_logx',
                title='City/Town Populations',
                xlabel='population',
                ylabel='CDF',
                xscale='log',
                legend=False)

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='populations_loglog',
                title='City/Town Populations',
                xlabel='populations',
                ylabel='Complementary CDF',
                yscale='log',
                xscale='log',
                legend=False)

    t = [math.log(x) for x in pops]
    t.sort()
    rankit.MakeNormalPlot(t, 'populations_rankit')


def main():
    MakeFigures()


if __name__ == '__main__':
    main()

