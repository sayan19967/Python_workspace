def wellbracketed(s):
	depth=0
	for i in range(0,len(s)):
		if s[i]=='(':
			depth=depth+1
		elif s[i]==')':
			depth=depth-1
	if depth==0:
		return True
	else:
		return False
