
# If Keyword
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif Keyword
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else Keyword
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# else without the elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 700
if a > b and c > a:
    print("Both conditions are True")

# Or
a = 200
b = 33
c = 7
if a > b or c > a:
    print("At least one of the conditions are True")




