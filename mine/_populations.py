import csv
import sys
import urllib


def ReadData(filename='populations.csv'):
    '''Reads the previously-downloaded contents of (filename), parses
    it as CSV and extracts all lines that seem to contain population
    information for a city or town.

    Args:
        filename: string name of file to read

    Returns:
        list of int populations
    '''
    try:
        fp = open(filename)
    except IOError:
        print 'Did not find pupulations.csv. You can download'
        print 'it from http://thinkstats.com/populations.csv'
        return []

    reader = csv.reader(fp)
    pops = []

    for t in reader:
        if len(t) != 11:
            continue

        try:
            name = t[0]
            if 'town' not in name and 'city' not in name:
                continue

            # use the second-to-last data point, which seems to
            # have fewer NAs
            pop = t[-2]
            pop = pop.replace(',', '')
            pop = int(pop)
            pops.append(pop)
        except:
            # if anything goes wrong, skip to the next open
            pass

    return pops


def main(scrpit, *args):
    pops = ReadData()

    for pop in pops:
        print pop


if __name__ == '__main__':
    main(*sys.argv)
