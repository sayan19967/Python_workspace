def ascending(list):
    #if len(l)%2 == 0:
    #    p=len(l)
    #else
    #    p=len(l)-1
    flag = 0
    if len(list)==0:
        return True
    elif len(list)==1:
        return True
    else:
        for i in range(0,len(list)-1):
            if list[i]>list[i+1]:
                flag = 1
    if flag == 0:
        return True
    else:
        return False
