def InsertionSort(seq):
    for i in range(len(seq)):
        pos = i
        while pos>0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos-1
    return(seq)




