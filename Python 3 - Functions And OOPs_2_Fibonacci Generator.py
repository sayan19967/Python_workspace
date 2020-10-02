def fib_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fs = fib_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
    
