#A Coroutine is generator which is capable of constantly receiving input data,
#process input data and may or may not return any output.

#Coroutines are majorly used to build better Data Processing Pipelines.

#Similar to a generator, execution of a coroutine stops when it reaches
#yield statement. A Coroutine uses send method to send any input value,
#which is captured by yield expression.

#TokenIssuer is a coroutine function, which uses yield to accept name as input.

#Execution of coroutine function begins only when next is called on coroutine t.

#This results in the execution of all the statements till a yield statement is encountered.

#Further execution of function resumes when an input is passed using send, and processes all
#statements till next yield statement.

# Example 1
##def TokenIssuer():
##    tokenId = 0
##    while True:
##        name = yield
##        tokenId += 1
##        print('Token number of', name, ':', tokenId)
##t = TokenIssuer()
##next(t)
##t.send('George')
##t.send('Rosy')
##t.send('Smith')


# Example 2
#In Example 2, the coroutine function TokenIssuer takes an argument,
#which is used to set a starting number for tokens.

#When coroutine t is closed, statements under GeneratorExit block are executed.

##def TokenIssuer(tokenId=0):
##    try:
##       while True:
##            name = yield
##            tokenId += 1
##            print('Token number of', name, ':', tokenId)
##    except GeneratorExit:
##        print('Last issued Token is :', tokenId)
##t = TokenIssuer(100)
##next(t)
##t.send('George')
##t.send('Rosy')
##t.send('Smith')
##t.close()


#As seen in Example1 and Example2, passing input to coroutine is possible only
#after the first next function call.

#Many programmers may forget to do so, which results in error.

#Such a scenario can be avoided using a decorator as shown in Example 3.
# Example 3
#In Example 3, coroutine_decorator takes care of calling next on the created coroutine t.

##def coroutine_decorator(func):
##    def wrapper(*args, **kwdargs):
##        c = func(*args, **kwdargs)
##        next(c)
##        return c
##    return wrapper
##
##@coroutine_decorator
##def TokenIssuer(tokenId=0):
##    try:
##        while True:
##            name = yield
##            tokenId += 1
##            print('Token number of', name, ':', tokenId)
##    except GeneratorExit:
##        print('Last issued Token is :', tokenId)
##t = TokenIssuer(100)
##t.send('George')
##t.send('Rosy')
##t.send('Smith')
##t.close()


# quiz

##def stringParser():
##    while True:
##        name = yield
##        (fname, lname) = name.split()
##        f.send(fname)
##        f.send(lname)
##
##def stringLength():
##    while True:
##        string = yield
##        print("Length of '{}' : {}".format(string, len(string)))
##
##
##f = stringLength(); next(f)
##
##s = stringParser()
##next(s)
##s.send('Jack Black')


# quiz

##def nameFeeder():
##    while True:
##        fname = yield
##        print('First Name:', fname)
##        lname = yield
##        print('Last Name:', lname)
##
##n = nameFeeder()
##next(n)
##n.send('George')
##n.send('Williams')
##n.send('John')


# Hackerrank - 1

# Define the coroutine function 'linear_equation' below.

##def linear_equation(a, b):
##    try:
##       while True:
##            x = yield
##            res = a * (x ** 2) + b
##            resStr = 'Expression, ' + str(a) + '*x^2 + ' + str(b) + ', with x being ' + str(x) + ' equals ' + str(res)
##            print(resStr)
##    except GeneratorExit:
##        print('')


# Hackerrank - 2

# Define 'coroutine_decorator' below

##def coroutine_decorator(coroutine_func):
##    def wrapper(*args, **kwdargs):
##        c = coroutine_func(*args, **kwdargs)
##        next(c)
##        return c
##    return wrapper
##    
### Define coroutine 'linear_equation' as specified in previous exercise
##@coroutine_decorator
##def linear_equation(a, b):
##    try:
##       while True:
##            x = yield
##            res = a * (x ** 2) + b
##            resStr = 'Expression, ' + str(a) + '*x^2 + ' + str(b) + ', with x being ' + str(x) + ' equals ' + str(res)
##            print(resStr)
##    except GeneratorExit:
##        print('')


# Hackerrank - 3

# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    
    while True:
        x = yield
        res = a * (x ** 2) + b
        resStr = 'Expression, ' + str(a) + '*x^2 + ' + str(b) + ', with x being ' + str(x) + ' equals ' + str(res)
        print(resStr)
    
    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)
    
def main(x):
    n = numberParser()
    n.send(x)

































































