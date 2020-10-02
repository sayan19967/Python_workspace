def rotatelist(s,k):
	if k>0:
		for i in range(1,k+1):
			s=s[len(s)-1:]+s[0:len(s)-1]
		return s
	else:
		return s
