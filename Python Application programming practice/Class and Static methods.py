#A method defined inside a class is bound to its object, by default.
#However, if the method is bound to a Class, then it is known as classmethod.
#Example 1 defines the method getCirclesCount,
#bound to an object of Circle class.

##class Circle(object):
##    no_of_circles = 0
##    def __init__(self, radius):
##        self.__radius = radius
##        Circle.no_of_circles += 1
##    def getCirclesCount(self):
##        return Circle.no_of_circles
##c1 = Circle(3.5)
##c2 = Circle(5.2)
##c3 = Circle(4.8)
##print(c1.getCirclesCount())     # -> 3
##print(c2.getCirclesCount())     # -> 3
##print(Circle.getCirclesCount(c3)) # -> 3
##print(Circle.getCirclesCount()) # -> TypeError


#Example 2 defines the classmethod getCirclesCount, bound to class Circle.

##class Circle(object):
##    no_of_circles = 0
##    def __init__(self, radius):
##        self.__radius = radius
##        Circle.no_of_circles += 1
##    @classmethod
##    def getCirclesCount(self):
##        return Circle.no_of_circles
##c1 = Circle(3.5)
##c2 = Circle(5.2)
##c3 = Circle(4.8)
##print(c1.getCirclesCount())     # -> 3
##
##print(c2.getCirclesCount())     # -> 3
##
##print(Circle.getCirclesCount()) # -> 3


#A method defined inside a class and not bound to either a class
####or an object is known as Static Method.
####
####Decorating a method using @staticmethod decorator makes it a static method.
####
####Consider the following two examples:
####
####Example1 defines the method square, outside the class definition of
####Circle, and uses it inside the class Circle.
####
####Example2 defines the static method square, inside the class
####Circle, and uses it.

# Example 1
##def square(x):
##        return x**2
##class Circle(object):
##    def __init__(self, radius):
##        self.__radius = radius
##    def area(self):
##        return 3.14*square(self.__radius)
##c1 = Circle(3.9)
##print(c1.area())
##print(square(10))

#Example 2
##class Circle(object):
##    def __init__(self, radius):
##        self.__radius = radius
##    @staticmethod
##    def square(x):
##        return x**2
##    def area(self):
##        return 3.14*self.square(self.__radius)
##c1 = Circle(3.9)
##print(c1.area())  
##print(square(10)) # -> NameError
##print(Circle.square(10))

#quiz
##class A:
##
##    @classmethod
##    def getC(self):
##        print('In Class A, method getC.')
##
##class B(A):
##    pass
##
##b = B()
##B.getC()
##b.getC()


#quiz
##def s1(x, y):
##    return x*y
##
##class A:
##
##    @staticmethod
##    def s1(x, y):
##        return x + y
##
##    def s2(self, x, y):
##        return s1(x, y)
##
##a = A()
##print(a.s2(3, 7))

#quiz
class A:

    @staticmethod
    def m1(self):
        print('Static Method')

    @classmethod
    def m1(self):
        print('Class Method')

A.m1()


## Hackerrank - 1
#Add Circle class implementation below
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)

##Hackerrank - 2
#Add Circle class implementation here
class Circle(object):
    __no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.__no_of_circles += 1
    @staticmethod
    def square(x):
        return x**2
    @classmethod
    def getCircleCount(pos):
        return Circle.__no_of_circles
    def area(self):
        return 3.14*self.square(self.__radius)
## Hackerrank - 3
#Add circle class implementation here
class Circle(object):
    __no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.__no_of_circles += 1
    @staticmethod
    def square(x):
        return x**2
    @classmethod
    def getCircleCount(pos):
        return Circle.__no_of_circles
    @staticmethod
    def getPi():
        return 3.14
    def area(self):
        return self.getPi()*self.square(self.__radius)





















