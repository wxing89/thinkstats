import brfss
import cPickle
import continuous
import Cdf
import math
import matplotlib
import matplotlib.pyplot as pyplot
import myplot
import random
import rankit
import sys
import survey
import thinkstats


class Respondents(brfss.Respondents):
    '''Respondents the respondent table.'''

    def MakeNormalModel(self, weights, root,
                        xmax=175,
                        xlabel='adult weight (kg)',
                        axis=None):
        cdf = Cdf.MakeCdfFromList(weights)

        pyplot.clf()

        t = weights[:]
        t.sort()
        mu, var = thinkstats.TrimedMeanVar(t)
        print 'n, Mean, Var', len(weights), mu, var
        
        sigma = math.sqrt(var)
        print 'Sigma', sigma

        xs, ps = continuous.RenderNormalCdf(mu, sigma, xmax)
        pyplot.plot(xs, ps, label='model', linewidth=4, color='0.7')

        xs, ps = cdf.Render()
        pyplot.plot(xs, ps, label='data',linewidth=2, color='blue')

        myplot.Save(root,
                    title='Adult weight',
                    xlabel=xlabel,
                    ylabel='CDF',
                    axis=axis or [0, xmax, 0, 1])

