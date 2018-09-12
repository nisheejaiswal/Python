import re

myString = "Send an email from this@email.com to test@yser.com 34 times"

# ^ Start
result = re.findall('^Send', myString)
print(result)

# [abc] Match  one character in the specified set
result = re.findall('[abc]', myString)
print(result)

# [0-9]+
result = re.findall('[0-9]+', myString)
print(result)

# [^a-z]+ anything not including inside the square bracket
result = re.findall('[^a-z]+', myString)
print(result)

# How to extract email using regular expressions.
# \S  Non-whitespace
result = re.findall('\S+@\S+', myString)
print(result)

# ^ Start
# $ Stop
# . Any character
# * Match one character 0+ times
# + Match one character 1+ times
# ? Non-greedy
# \s Whitespace
# [abc] Match one character in the specified set
# [^abc] Match one character not in the specified set