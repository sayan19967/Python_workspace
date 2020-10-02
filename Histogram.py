def histogram(list):
    list1 = []
    for value in list:
        if value not in list1:
            list1.append(value)
    p = [0 for i in range(len(list1))]
    count = 0
    for j in range(len(list1)):
        for k in range(len(list)):
            if list1[j] == list[k]:
                count = count + 1
                p[j] = count
        count = 0
    for i in range(len(list1)):
        #temp = p[i]
        for j in range(i,len(p)-1):
            if p[i] > p[j+1]:
                (list1[i],list1[j+1]) = (list1[j+1],list1[i])
                (p[i],p[j+1]) = (p[j+1],p[i])
            elif p[i] == p[j+1]:
                if list1[i] > list1[j+1]:
                    (list1[i],list1[j+1]) = (list1[j+1],list1[i])
    list2 = [(list1[i],p[i]) for i in range(len(p))]
    return(list2)
    
                
                
            
            
        
    
            
    
