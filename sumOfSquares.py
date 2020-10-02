from math import *
>>> def sumOfSquares(m):
        flag=0
	for i in range(1,m):
		n = m -(i*i)
		for j in range(1,n):
			if n == j*j:
                            flag = flag+1
                            return True
        if flag==0:
            return False
    
                        
