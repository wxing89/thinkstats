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

    print scores, index_start

    if index_start == rank:
        return scores[index_start - 1]
    elif index_start > rank:
        print '>', scores[:index_start], rank
        return SelectScore(scores[:index_start], rank)
    else:
        print '<', scores[index_start:], rank - index_start
        return SelectScore(scores[index_start:], rank - index_start)

def swap(scores, i, j):
    if i == j:
        return
    temp = scores[j]
    scores[j] = scores[i]
    scores[i] = temp

l = [55, 66, 77, 88, 99]

print SelectScore(l,5)