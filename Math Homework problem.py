def minNum(threshold, points):
    count = 1
    n = 0
    print(points)
    length = len(points)
    if not points[length-1] - points[0] < threshold:
        while n < length:
            if n >= length - 1:
                break
            elif points[n+1] - points[0] >= threshold:
                count = count + 1
                n = n + 1
                break
            elif n < length - 2:
                count = count + 1
                n = n + 2
    else:
        count = length

    diff = points[n] - points[0]
    print(n)
    print(diff)
    if not diff >= threshold:
        count = length
    return count

l1 = [82,112,134,178,206,229,238,278,293,335]
l2 = [1,2,3,5,8,8,8,8,8]
count = minNum(4, l2)
print(count)
        
            
        
            
