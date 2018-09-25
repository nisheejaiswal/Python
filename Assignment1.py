import requests
import json
import sys
import os


def FetchData():
    # HTTP GET Request
    base_url_get = "https://httpbin.org/get"
    response = requests.get(base_url_get)
    print(response)
    s = response.text
    # define the name of the directory to be created
    with open("C://Data//FetchData.txt", "w") as f:
        f.write(s)


def CreateNewResource():
    # HTTP POST REQUEST
    base_url_post = "https://httpbin.org/post"
    file = open("C:\\Users\\kiit1\\Desktop\\CreateUser.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(base_url_post, request_json)
    print(response)
    s = response.text

    with open("C://Data//CreateNewResource.txt", "w") as f:
        f.write(s)


def PutRequest():
    # HTTP PUT Request
    r = requests.put("https://httpbin.org/put", data={'key': 'value'})
    print(r)
    s = r.text

    with open("C://Data//CreateNewResource.txt", "w") as f:
        f.write(s)


def DeleteRequest():
    # HTTP DELETE Request
    r = requests.delete("https://httpbin.org/delete")
    print(r)


def PassingParam():
    # Passing Parameters In URLs
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', params=payload)
    s= r.url

    with open("C://Data//PassingParam1.txt", "w") as f:
        f.write(s)


def main():
    print("API Request Modules are as follows:-")
    FetchData()
    CreateNewResource()
    PutRequest()
    DeleteRequest()
    PassingParam()



if __name__=="__main__":
    main()
