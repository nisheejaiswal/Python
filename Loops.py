
# The while Loop
print("The while Loop")
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
print("The break Statement:-")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
print("The continue statement:-")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# For Loops
print("The For Loops")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# The break Statement
print("The break Statement:-")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement\
print("The continue statement:-")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
print("The range() function:-")
for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2, 30, 3):
    print(x)

# Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for x in adj:
        for y in fruits:
            print(x, y)





