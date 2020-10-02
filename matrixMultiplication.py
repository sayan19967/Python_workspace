def matmult(m1,m2):
    r1 = len(m1)
    r2 = len(m2)
    c1 = len(m1[0])
    c2 = len(m2[0])
    mult = [[0 for row in range(len(m2[0]))] for col in range(len(m1))]
    sum = 0
    if c1 == r2:
        for i in range(0,r1):
            for j in range(0,c2):
                for k in range(0,r2):
                    sum = sum + m1[i][k]*m2[k][j]
                mult[i][j] = sum
                sum = 0
    return mult
