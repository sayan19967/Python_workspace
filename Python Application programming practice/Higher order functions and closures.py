###function as data
##
##def greet():
##    return 'Hello Everyone!'
##print(greet())
##wish = greet       # 'greet' function assigned to variable 'wish'
##print(type(wish))   
##print(wish())  


#function as argument
##def add(x, y):
##    return x + y
##def sub(x, y):
##   return x - y
##def prod(x, y):
##    return x * y
##def do(func, x, y):
##   return func(x, y)
##print(do(add, 12, 4))  # 'add' as arg
##print(do(sub, 12, 4))  # 'sub' as arg
##print(do(prod, 12, 4))  # 'prod' as arg


#in the following case, the return val of outer func is the return val of inner func

##def outer():
##
##    def inner():
##
##        s = 'Hello world!'
##        print('hi')
##        return s
##
##    print('hi again')
##
##    return inner()    
##
##print(outer())



#Returning an actual function
##def outer():
##
##    def inner():
##
##        s = 'Hello world!'
##
##        return s            
##
##        
##
##    return inner   # Removed '()' to return 'inner' function itself
##
##    
##
##print(outer()) #returns 'inner' function
##
##func = outer() 
##
##print(type(func))
##
##print(func()) # calling 'inner' function


#Closures
##def multiple_of(x):
##    def multiple(y):
##        return x*y
##    return multiple
##c1 = multiple_of(5)  # 'c1' is a closure
##c2 = multiple_of(6)  # 'c2' is a closure
##print(c1(4))
##print(c2(4))



#Hackerrank problem - 1
##def detecter(element):
##
##    #Write isIn implementation 
##    def isIn(sequence):
##        if element in sequence:
##            return True
##        else:
##            return False
##
##    return isIn
##
###Write closure function implementation for detect30 and detect45
##detect30 = detecter(30)
##detect45 = detecter(45)



#Hackerrank problem - 2
# Add the factory function implementation here
##def factory(n = 0):
##    def current():
##        return n
##    def counter():
##        return n + 1
##
##    return (current, counter)
##
##f_current, f_counter = factory(int(input()))













































