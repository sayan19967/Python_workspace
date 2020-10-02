###########Descriptor
########## Example 1 : The descriptor, EmpNameDescriptor is defined
#to manage empname attribute. It checks if the value of
#empname attribute is a string or not.
##class EmpNameDescriptor:
##    def __get__(self, obj, owner):
##        return self.__empname
##    def __set__(self, obj, value):
##        if not isinstance(value, str):
##            raise TypeError("'empname' must be a string.")
##        self.__empname = value


############ Example 2 : The descriptor, EmpIdDescriptor is
#defined to manage empid attribute.
##class EmpIdDescriptor:
##    def __get__(self, obj, owner):
##        return self.__empid
##    def __set__(self, obj, value):
##        if hasattr(obj, 'empid'):
##            raise ValueError("'empid' is read only attribute")
##        if not isinstance(value, int):
##            raise TypeError("'empid' must be an integer.")
##        self.__empid = value

##############Employee class is defined such that, it creates empid and
#empname attributes from descriptors EmpIdDescriptor and EmpNameDescriptor.
##class Employee:
##    empid = EmpIdDescriptor()           
##    empname = EmpNameDescriptor()       
##    def __init__(self, emp_id, emp_name):
##        self.empid = emp_id
##        self.empname = emp_name

######### You can observe that accessing attributes empid and empname
####appear as if you are accessing them directly.However when executing the
####expression e1.empid = 76347322, the __set__ method defined in
####EmpIdDescriptor is executed and raises
####"ValueError: 'empid' is read only attribute".
##e1 = Employee(123456, 'John')
##print(e1.empid, '-', e1.empname)  
##e1.empname = 'Williams'
##print(e1.empid, '-', e1.empname)
##e1.empid = 76347322



#############Properties
#Descriptors can also be created using property() type.
#It is easy to create a descriptor for any attribute using property().
##class Employee:
##    def __init__(self, emp_id, emp_name):
##        self.empid = emp_id
##        self.empname = emp_name
##    def getEmpID(self):
##        return self.__empid
##    def setEmpID(self, value):
##       if not isinstance(value, int):
##            raise TypeError("'empid' must be an integer.")
##        self.__empid = value
##    empid = property(getEmpID, setEmpID)
##
##     def getEmpName(self):
##
##        return self.__empname
##
##    def setEmpName(self, value):
##
##        if not isinstance(value, str):
##
##            raise TypeError("empname' must be a string.")
##
##        self.__empname = value
##
##    def delEmpName(self):
##
##        del self.__empname
##
##    empname = property(getEmpName, setEmpName, delEmpName)
##
##e1 = Employee(123456, 'John')
##
##print(e1.empid, '-', e1.empname)    # -> '123456 - John'
##
##del e1.empname    # Deletes 'empname'
##
##print(e1.empname) #Raises 'AttributeError'


##Property Decorator
#get and set methods of empid attribute are decorated with property.
##class Employee:
##    def __init__(self, emp_id, emp_name):
##        self.empid = emp_id
##        self.empname = emp_name
##    @property
##    def empid(self):
##        return self.__empid
##    @empid.setter
##    def empid(self, value):
##        if not isinstance(value, int):
##            raise TypeError("'empid' must be an integer.")
##        self.__empid = value
##
##    @property
##    def empname(self):
##        return self.__empname
##    @empname.setter
##    def empname(self, value):
##        if not isinstance(value, str):
##            raise TypeError("'empname' must be a string.")
##        self.__empname = value
##    @empname.deleter
##    def empname(self):
##        del self.__empname
##
##e1 = Employee(123456, 'John')
##print(e1.empid, '-', e1.empname)    # -> '123456 - John'
##del e1.empname    # Deletes 'empname'
##print(e1.empname) #Raises 'AttributeError'


# quiz
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


#quiz
##class A:
##
##    def __init__(self, value):
##        self.x = value
##
##    @property
##    def x(self):
##        return self.__x
##
##    @x.setter
##    def x(self, value):
##        if not isinstance(value, (int, float)):
##            raise ValueError('Only Int or float is allowed')
##        self.__x = value
##
##a = A(7)
##a.x = 'George'
##print(a.x)



## Hackerrank problem
# Add Celsius class implementation below.
class Celsius:

    def __get__(self, obj, owner):
        return 5 * (obj.fahrenheit - 32) / 9

    def __set__(self, obj, value):
        obj.fahrenheit = 32 + 9 * value / 5
# Add temperature class implementation below.  
class Temperature:

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f

t = Temperature(212)
print(t.celsius)
t.celsius = 0
print(t.fahrenheit)





















