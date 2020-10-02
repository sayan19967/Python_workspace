Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def gcd(m,n):
	i = min(m,n)
	while i>0:
		if (m%i)==0 and (n%i)==0:
			return(i)
		else:
			i = i-1
