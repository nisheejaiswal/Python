
# List - ordered and changeable
listsample = ["apple", "banana", "cherry"]
print(listsample)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# List length
print(len(thislist))

# Add Items
thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

# Remove Item
thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

"""
We can delete the entire list by using -
del thislist
"""

"""
We can empty the entire list by using -
thislist.clear()
"""

# The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
