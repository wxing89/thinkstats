'''Exercise 4.7 

The Wechsler Adult Intelligence Scale is a test that is
intended to measure intelligence. Results are transformed 
so that the distribution of scores in the general population 
is normal with m = 100 and s = 15.

Use erf.NormalCdf to investigate the frequency of rare events 
in a normal distribution. What fraction of the population has 
an IQ greater than the mean? What fraction is over 115? 130? 145?

A "six-sigma" event is a value that exceeds the mean by 6 
standard devia-tions, so a six-sigma IQ is 190. In a world of 
6 billion people, how many do we expect to have an IQ of 190 or more?
'''


import random

import erf
import myplot


# mu = 100
# sigma = 15
def main():
    print 'IQ probabilities:'
    print 'greater than the mean:', 1 - erf.NormalCdf(100, mu=100, sigma=15)
    print 'greater than 115:', 1 - erf.NormalCdf(115, mu=100, sigma=15)
    print 'greater than 130:', 1 - erf.NormalCdf(130, mu=100, sigma=15)
    print 'greater than 145:', 1 - erf.NormalCdf(145, mu=100, sigma=15)

    print 'Populations size:'
    print 'IQ greater than Einstain:', 1/(1 - erf.NormalCdf(160, mu=100, sigma=15))
    print 'IQ greater than 197:', 1/(1 - erf.NormalCdf(197, mu=100, sigma=15))


if __name__ == '__main__':
    main()
