
# Creating a Function
def my_function():
    print("Hello from a function")

# Calling a Function
def my_function():
    print("Hello from a function")

my_function()

# Parameters
def my_function(fname):
    print(fname + "Refresh")

my_function("Email")
my_function("Facebook")
my_function("Twitter")

# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))