

# Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))  # Here we specify the characters we want to return

# Read Lines
f = open("demofile.txt", "r")
print(f.readline())  # We can read only the first line of the file

# By looping , we can read the whole file, line by line
f = open("demofile.txt", "r")
for x in f:
    print(x)