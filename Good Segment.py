def goodSegment(badNumbers, lower, upper):
    l = list(range(lower,upper+1))
    badNumbers.sort()
    print(badNumbers)
    index1 = 0
    size = []
    for i in badNumbers:
        print(i)
        if i in l:
            print(i)
            index2 = l.index(i)
            tempList = l[index1:index2]
            size.append(len(tempList))
            index1 = index2 + 1

    tempList = l[index1:]
    size.append(len(tempList))
    size.sort()
    return size[-1]

size = goodSegment([5,4,2,15], 1, 10)
print(size)
            
