import json

data = '''{
    "name": "Aakash",
    "phone": {
        "type": "national",
        "number": "99999999"
    }
}
'''

details = json.loads(data)

print("Name: ", details["name"])
print("Number: ", details["phone"]["number"])




import json

path = "C://Data//"
n = "Name : " + details["name"] + " Phone Number: " + details["phone"]["number"]
s = json.dumps(n)
with open(path+"persons.txt","w") as f:
    f.write(s)