
# File Write

# To append
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# To overwrite
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
