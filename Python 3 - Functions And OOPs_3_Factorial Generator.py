def factorial_gen():
    a,b = 1,0
    while True:
        yield a
        b += 1
        a = a * b

fs = factorial_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
