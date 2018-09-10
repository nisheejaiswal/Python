
# Dictonary - unordered, changeable and indexed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Accessing Items
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

# Change Values
thisdict["year"] = 2018
print(thisdict)

# Loop Through a Dictionary
for x in thisdict:
    print(x)
# print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])
# OR we can use values() function to return values of a dictionary
for x in thisdict.values():
    print(x)
# Loop through both keys and values, by using items() function:
for x, y in thisdict.items():
    print(x, y)

# Dictionary Length
print(len(thisdict))

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
del thisdict["model"]
print(thisdict)

thisdict.pop("year")
print(thisdict)

# popitem() method removes the last item
thisdict.popitem()
print(thisdict)

# clear() - empties the dictionary
thisdict.clear()

# del - can also delete the dictionary completely
del thisdict

# The dict() Constructor
thisdict = dict(brand="Ford", model="Musang", year=1964)
print(thisdict)









