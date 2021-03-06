# Exercise 3.10 
#
# The numbers generated by random.random are supposed to be uniform 
# between 0 and 1; that is, every value in the range should have the 
# same probability.
#
# Generate 1000 numbers from random.random and plot their PMF and CDF.
# Can you tell whether they are uniform?
#
# You can read about the uniform distribution at 
# http://wikipedia.org/wiki/Uniform_distribution_(discrete).

import random

import Pmf
import Cdf
import myplot

def main():
    num_list = [random.randint(0, 99) for i in range(1000)]
    pmf = Pmf.MakeHistFromList(num_list, 'random numbers pmf')
    cdf = Cdf.MakeCdfFromList(num_list, 'random numbers cdf')

    myplot.Pmf(pmf)
    myplot.Save(root='random_numbers_pmf',
                title='Pmf of random numbers',
                xlabel='number',
                ylabel='probability')

    myplot.Cdf(cdf)
    myplot.Save(root='random_numbers_Cdf',
                title='Cdf of random numbers',
                xlabel='number',
                ylabel='probability')


if __name__ == '__main__':
    main()