
# Set - unordered and unindexed
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset) # Check if "banana" is present in the set

"""
Once a set is created, we cannot change its items, 
but we can add new items.
"""

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("banana")
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

# clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)





