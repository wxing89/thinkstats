"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank

scores = [55, 66, 77, 88, 99]
your_score = 88

print 'score, percentile rank'
for score in scores:
    print score, PercentileRank(scores, score)
print

def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores.sort()
    index = percentile_rank * (len(scores) - 1) / 100
    return scores[index]

def Percentile3(scores, percentile_rank):
    index = percentile_rank * (len(scores) - 1) / 100
    return SelectScore(scores, index + 1)

def SelectScore(scores, rank):
    if len(scores) == 1:
        return scores[0]
    
    if len(scores) == 2:
        if scores[0] > scores[1]:
            swap(scores, 0, 1)
        if rank == 1:
            return scores[0]
        else:
            return scores[1]
    
    index_start = 1
    index_end = len(scores) - 1
    
    while index_start < index_end:
        if scores[index_start] > scores[0]:
            swap(scores, index_start, index_end)
            index_end -= 1
        else:
            index_start += 1

    if scores[index_start] < scores[0]:
        swap(scores, 0, index_start)
    else:
        swap(scores, 0, index_start - 1)

    if index_start == rank:
        return scores[index_start - 1]
    elif index_start > rank:
        return SelectScore(scores[:index_start], rank)
    else:
        return SelectScore(scores[index_start:], rank - index_start)

def swap(scores, i, j):
    if i == j:
        return
    temp = scores[j]
    scores[j] = scores[i]
    scores[i] = temp

print 'prank, score, score, score'
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print percentile_rank, 
    print Percentile(scores, percentile_rank),
    print Percentile2(scores, percentile_rank),
    print Percentile3(scores, percentile_rank)
