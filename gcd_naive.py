def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    fm=[]
    for i in range(1,m+1):
        if m%i == 0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if n%j == 0:
            fn.append(j)
    cf=[]
    for f in fn:
        if f in fm:
            cf.append(f)
    return(cf[-1])
