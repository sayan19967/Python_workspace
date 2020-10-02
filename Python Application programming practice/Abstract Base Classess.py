#An Abstract Base Class or ABC mandates the derived classes to
#implement specific methods from the base class.
#It is not possible to create an object from a defined ABC class.
#Creating objects of derived classes is possible only when derived
#classes override existing functionality of all
#abstract methods defined in an ABC class.

#In Python, an Abstract Base Class can be created using module abc.
#In Example 1, Abstract base class Shape is defined with two abstract
#methods area and perimeter.

##from abc import ABC, abstractmethod
##class Shape(ABC):
##    @abstractmethod
##    def area(self):
##        pass
##    @abstractmethod
##    def perimeter(self):
##        pass
##
##class Circle(Shape):
##    def __init__(self, radius):
##        self.__radius = radius
##    @staticmethod
##    def square(x):
##        return x**2
##    def area(self):
##        return 3.14*self.square(self.__radius)
##    def perimeter(self):
##        return 2*3.14*self.__radius
##c1 = Circle(3.9)
##print(c1.area())
##print(c1.perimeter())
#s1 = Shape()   ##will throw TypeError as can't instantiate abstract class


#quiz
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

#quiz
##from abc import ABC, abstractmethod
##
##class A(ABC):
##    @abstractmethod
##    def m1():
##        print('In class A.')
##
##a = A()
##a.m1()


#quiz
##from abc import ABC, abstractmethod
##
##class A(ABC):
##
##    @classmethod
##    @abstractmethod
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


# Hackerrank -1
from abc import ABC, abstractmethod
# Define the abstract class 'Animal' below
# with abstract method 'say'
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass
# Define class Dog derived from Animal
# Also define 'say' method inside 'Dog' class
class Dog(Animal):
    msg = 'I speak Booooo'
    @classmethod
    def say(self):
        return self.msg





















































































