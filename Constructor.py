
# Python Constructor Example
class ComplexNumber:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

c1 = ComplexNumber(5,6)
c1.getData()

"""
 We can create a new attribute for an object 
 and read it well at the time of defining the values.
"""
c2 = ComplexNumber(11)
c2.attr = 12
(c2.real, c2.imag, c2.attr)

# Non Parameterizedd Constructor
class Student:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)

student = Student()
student.show("Nishee")

# Parameterizedd Constructor
class Students:
    # Constructor - non parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)

students = Students("Nishee")
students.show()