#quiz 1

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

# quiz 2

##from abc import ABC, abstractmethod
##
##class A(ABC):
##
##    @abstractmethod
##    def m1(self):
##        print('In class A, Method m1.')
##
##class B(A):
##
##    @staticmethod
##    def m1(self):
##        print('In class B, Method m1.')
##
##b = B()
##B.m1(b)


# quiz 3

##class A:
##
##    def __init__(self, val):
##        self.x = val
##
##    @property
##    def x(self):
##        return self.__x
##
##    @x.setter
##    def x(self, val):
##        self.__x = val
##        
##    @x.deleter
##    def x(self):
##        del self.__x
##
##a = A(7)
##del a.x
##print(a.x)

# quiz 4

##import re
##print(re.sub(r'[aeiou]', 'X', 'abcdefghij'))


# quiz 5

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


# quiz 6

##from abc import ABC, abstractmethod
##
##class A(ABC):
##
##    
##    
##    @abstractmethod
##    @classmethod
##    def m1(self):
##        print('In class A, Method m1.')
##
##class B(A):
##
##    @classmethod
##    def m1(self):
##        print('In class B, Method m1.')
##
##b = B()
##b.m1()
##B.m1()
##A.m1()


# quiz 7

##class A:
##
##    def __init__(self, x):
##        self.__x = x
##
##    @property
##    def x(self):
##        return self.__x
##
##a = A(7)
##a.x = 10
##print(a.x)


# quiz 8

class A:

    def __init__(self, value):
        self.x = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Only Int or float is allowed')
        self.__x = value

a = A(7)
a.x = 'George'
print(a.x)




























