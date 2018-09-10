# 'hello' and "hello" are same

print("Hello, World!!!")

a = "Hello, World!"

#To get the character at position 1
print(a[1])

#To get the characters from position 2 to position 5(not included)
print(a[2:5])

# strip() method removes any whitespace from the beginning or the end
print(a.strip())

# len() method returns the length of a string
print(len(a))

# lower() method return the string in lower casw
print(a.lower())

# upper() method returns the string in upper case
print(a.upper())

# replace() method replaces a string with another string
print(a.replace("H", "J"))

# split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))

