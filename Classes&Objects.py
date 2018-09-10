
# Create a Class
class MyClass:
    x= 5

# Create Object
p1 = MyClass()
print(p1.x)

# The _init_() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Obh=ject Properties
p1.age = 40

# Delete Objects
del p1



