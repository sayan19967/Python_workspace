def alternating(list):
    p=len(list)
    flag = 0
    if p == 0:
        return True
    elif p == 1:
        return True
    elif list[0]<list[1]:
        for i in range(0,p-2):
            if i%2 == 0:
                if (list[i]>=list[i+1] or list[i+1]<=list[i+2]):
                    flag = 1
                    break
            else:
                if (list[i]<=list[i+1] or list[i+1]>=list[i+2]):
                    flag = 1
                    break
    elif list[0]>list[1]:
        for i in range(0,p-2):
            if i%2 == 0:
                if (list[i]<=list[i+1] or list[i+1]>=list[i+2]):
                    flag = 1
                    break
            else:
                if (list[i]>=list[i+1] or list[i+1]<=list[i+2]):
                    flag = 1
                    break
    if flag == 0:
        return True
    else:
        return False
    
    
    
