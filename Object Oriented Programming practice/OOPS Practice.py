class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
          
##
##class Employee(Person):
##    employees = []
##    def __init__(self,fname,lname,empid):
##        Person.__init__(self,fname,lname)
##        self.empid = empid
##        Employee.employees.append(self)
##
##
##
##p_parent = Person('sayan','halder')
##p_emp = Employee('soham','chakraborty',2)
##print(p_parent.fname)
##print(p_emp.fname + str(p_emp.empid))
##print(p_emp.employees[0].empid)
##itr = iter(p_emp.employees)
##print(next(itr).fname)
##p1 = Employee('naruto','uzumaki','as201')
##print(p1.empid)
##print(p_emp.employees[0].empid)
##print(p_emp.employees[1].empid)
##print(p_emp.employees)
##

        
#inheriting built in types in python
class EmployeesList(list):

    def search(self,name):
        matching_emp = []
        for employee in self:
            if name in employee.fname:
                matching_emp.append(employee.fname)
        return matching_emp

##class Employee(Person):
##    all_employees = EmployeesList()
##    def __init__(self,fname,lname,empid):
##        Person.__init__(self,fname,lname)
##        self.empid = empid
##        Employee.all_employees.append(self)
##
##e1 = Employee('sayan','halder',1)
##e2 = Employee('soham','chakraborty',2)
##e3 = Employee('sandy','chakraborty',2)
##print(Employee.all_employees.search('an'))


#polymorphism example
##class Employee(Person):
##    all_employees = EmployeesList()
##    def __init__(self,fname,lname,empid):
##        Person.__init__(self,fname,lname)
##        self.empid = empid
##        Employee.all_employees.append(self)
##    def getSalary(self):
##        return 'you get monthly salary'
##    def getBonus(self):
##        return 'you are eligible for bonus'
##
##class ContractEmployee(Employee):
##    def getSalary(self):
##        return 'you do not get salary'
##    def getBonus(self):
##        return 'you are not eligible for bonus'
##
##e1 = Employee('sayan','halder',1)
##e2 = ContractEmployee('soham','chakraborty',2)
##print(e1.getBonus())
##print(e2.getBonus())


#abstraction and encapsulation
##class Employee(Person):
##    all_employees = EmployeesList()
##    def __init__(self,fname,lname,empid):
##        Person.__init__(self,fname,lname)
##        self.__empid = empid
##    def getEmpid(self):
##        return self.__empid
##
##
##e1 = Employee('sayan','halder',484)
##print(e1.getEmpid())
##print(e1._empid)

import math
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return 'point : ({}, {}, {})'.format(self.x,self.y,self.z)
    def distance(self, other):
        distance = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)
        return distance
    def __add__(self, other):
        return self.x + other.x,self.y + other.y,self.z + other.z
       


        
p1 = Point(4,2,9)
p2 = Point(4,5,6)
p3 = Point(-2,-1,4)
##distance = Point.distance(p2,p3)
l = p2 + p3
print(type(l))
print(p2 + p3)


##import unittest
##def isEven(n):
##    if n % 2 == 0:
##        return True
##    else:
##        return False
##ans = isEven(43)
##
##class TestIsEvenMethod(unittest.TestCase):
##    def test_isEven1(self):
##        self.assertEqual(False, isEven(5))
##    def test_isEven2(self):
##        self.assertEqual(True, isEven(10))
##    def test_isEven3(self):
##        self.assertRaises(TypeError, isEven('hello'))
##
##unittest.main()


##36 + '20'
##10 + (1/0)
##try:
##    a = pow(2, 4)
##    print("Value of 'a' :", a)
##    b = pow(2, 'hello')   # results in exception
##    print("Value of 'b' :", b)
##except Exception as e:
##    print(e)
##print('Out of try ... except.')
##
##try:
##    a = 2; b = 'hello'
##    if not (isinstance(a, int)
##            and isinstance(b, int)):
##        raise TypeError('Two inputs must be integers.')
##    c = a**b
##except TypeError as e:
##    print(e)
##
##class CustomError(Exception):
##    def __init__(self, value):
##        self.value = value
##    def __str__(self):
##        return str(self.value)
##try:
##    #raise CustomError('custom error')
##    pass
##except Exception as e:
##    print(e)
##else:
##    print('inside else')
##finally:
##    print('finally')



##a = int(input())
##if a<0 or a>100:
##    try:
##        raise ValueError()
##    except ValueError as e:
##        print('Input integer value must be between 0 and 100.')

##a = input()
##if len(a)>10:
##    try:
##        raise ValueError()
##    except ValueError as e:
##        print('Input String contains more than 10 characters.')

##try:
##    file = open('unknown_file.txt')
##except Exception as e:
##    print('File not found')


##class RadiusInputError(Exception):
##    def __init__(self, value):
##        self.value = "'" + str(value) + "' is not a number"
##    def __str__(self):
##        return str(self.value)
##
##class Circle:
##    def __init__(self,r):
##        if not isinstance(r, int):
##            try:
##                raise RadiusInputError(r)
##            except Exception as e:
##                print(e)
##        else:
##            self.r = r
##
##c1 = Circle('hello')


##groupby object iteration

##from itertools import groupby
##numbers = [10, 13, 16, 22, 9, 4 , 37]
##d = {'even':[], 'odd':[]}
##for k,g in groupby(numbers, lambda x: x % 2):
##        if k:
##            d['odd'].extend(g)
##        else:
##            d['even'].extend(g)
##print(d)
##
##
####calender module
##
##import calendar
##
##def find_five_sunday_months(year):
##    calendar.setfirstweekday(calendar.SUNDAY)
##    five_sunday_months = []
##    for month in range(1, 13):
##        calendar_month = calendar.monthcalendar(year, month)
##        # If you're counting Sunday as the first day of the week, then any month that extends into
##        # six weeks, or starts on a Sunday and extends into five weeks, will contain five Sundays.
##        if len(calendar_month) == 6 or (len(calendar_month) == 5 and calendar_month[0][0] == 1):
##            five_sunday_months.append(calendar.month_abbr[month])
##
##    return five_sunday_months
##
##print (find_five_sunday_months(2018))
##
##
###time module
##import timeit
##def f1():
##    f= [i**2 for i in range(1,21)]
##    return f
##def f2():
##    g = (x**2 for x in range(1,21))
##    yield g
## 
##s1 = timeit.timeit(stmt="f1()",setup="from __main__ import f1",number=100000)
##print(s1)
##s2 = timeit.timeit(stmt="next(f2())",setup="from __main__ import f2",number=100000)
##print(s2)


l = {i:j for i in "abcd" for j in "kiwi"}
print(l)


class A:
    def __init__(self):
        print('one')

    def f(self):
        print(float())
        print(hex(-255))

class B(A):
    def __init__(self):
        print('two')

    def f(self):
        print(float())
        print(hex(-42))

x = B()
x.f()


l1 =[x*y for x, y in zip([3,4],[5,6])]
print(l1)























    




















    




















