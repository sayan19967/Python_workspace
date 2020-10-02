#Decorators
##@outer
##
##def greet():
##
##   pass

################## Example 1 ####################################
#First one shows the creation of closure function
#wish using the higher order function outer.
##def outer(func):
##    def inner():
##        print("Accessing :", 
##                  func.__name__)
##        return func()
##    return inner
##def greet():
##   print('Hello!')
##wish = outer(greet)
##wish()





######################## Example 2 #############################
#The second one shows the creation of decorator function outer,
#which is used to decorate function greet.
#This is achieved with a small change to Example1.
##def outer(func):
##   def inner():
##        print("Accessing :", 
##                  func.__name__)
##        return func()
##    return inner
##def greet():
##   return 'Hello!'
##greet = outer(greet) # decorating 'greet'
##greet()  # calling new 'greet'



######################## Example 3 ###############################
#Third one displays decorating the greet function with
#decorator function, outer, using @ symbol.
##def outer(func):
##    def inner():
##        print("Accessing :", 
##                func.__name__)
##        return func()
##    return inner
##@outer
##def greet():
##    print('Hello!')
##    return 'Hello!'
##greet()


#quiz 1
##def decorator_func(func):
##    def wrapper(*args, **kwdargs):
##        return func(*args, **kwdargs)
##    wrapper.__name__ = func.__name__
##    return wrapper
##
##
##@decorator_func
##def square(x):
##    return x**2
##
##print(square.__name__)

#quiz 2
##def bind(func):
##    func.data = 9
##    return func
##
##@bind
##def add(x, y):
##    return x + y
##
##print(add(3, 10))
##print(add.data)

#quiz 3
##def smart_divide(func):
##    def wrapper(*args):
##        a, b = args
##        if b == 0:
##            print('oops! cannot divide')
##        return func(*args)
##    return wrapper
##@smart_divide
##def divide(a, b):
##    return a / b
##
##print(divide.name)
##print(divide(4, 16))
##print(divide(8,0))


#quiz
##from functools import wraps
##
##def decorator_func(func):
##    @wraps(func)
##    def wrapper(*args, **kwargs):
##        return func(*args, **kwargs)
##    return wrapper
##
##@decorator_func
##def square(x):
##    return x**2
##
##print(square.__name__)


#quiz
##def star(func):
##    def inner(args, **kwargs):
##        print("" * 3)
##        func(args, **kwargs)
##        print("" * 3)
##        return inner
##
##def percent(func):
##    def inner(*args, **kwargs):
##        print("%" * 3)
##        func(*args, **kwargs)
##        print("%" * 3)
##        return inner
##
##@star
##@percent
##def printer(msg):
##    print(msg)
##
##printer("Hello")


########################### Hackerrank - 1 ################################
##def log(func):
##    def inner(*args, **kwdargs):
##        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
##                                                                                args,
##                                                                                kwdargs)
##        return str_template + "\n" + str(func(*args, **kwdargs))
##    return inner    
##    
##
##@log
##def greet(msg):
##    'Greeting Message : ' + msg
##    return ''
##print(greet('sayan'))


######################## Hackerrank - 2 ###########################
##def log(func):
##    def inner(*args, **kwdargs):
##        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
##                                                                                args,
##                                                                                kwdargs)
##        return str_template + "\n" + str(func(*args, **kwdargs))
##    return inner
##
###Add greet function definition here
##@log
##def average(n1,n2,n3):
##    return (n1 + n2 + n3)/3


######################### Hackerrank - 3 ########################
#Define and implement bold_tag
##def bold_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<b>'+func(*args, **kwdargs)+'</b>'
##        
##    return inner   
##@bold_tag
##def say(msg):
##    return msg

########################## Hackerrank - 4 ###########################
##def italic_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<i>'+func(*args, **kwdargs)+'</i>'
##        
##    return inner
##
###Implement italic_tag below
##
##@italic_tag
##def say(msg):
##    return msg


########################### Hackerrank - 5 ##########################
##def bold_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<b>'+func(*args, **kwdargs)+'</b>'
##        
##    return inner
##
##def italic_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<i>'+func(*args, **kwdargs)+'</i>'
##        
##    return inner
##    
###Add greet() function definition
##@italic_tag
##def greet(msg):
###    return input()
##    return msg
##
##print(greet('sayan'))


################# Hackerrank - 6 ##########################
##def bold_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<b>'+func(*args, **kwdargs)+'</b>'
##        
##    return inner
##
##def italic_tag(func):
##    
##    def inner(*args, **kwdargs):
##        return '<i>'+func(*args, **kwdargs)+'</i>'
##        
##    return inner
##    
###Add greet() implementation here
##
##@italic_tag
##@bold_tag
##def greet():
##    return input()
##
##print(greet())


















