
# Make a  Request

import requests
r = requests.get("https://httpbin.org")
print(r)

# HTTP POST Request
r = requests.post("https://httpbin.org/post", data = {'key':'value'})
print(r)

# HTTP PUT Request
r = requests.put("https://httpbin.org/put", data = {'key':'value'})
print(r)

# HTTP DELETE Request
r = requests.delete("https://httpbin.org/delete")
print(r)

# HTTP HEAD Request
r = requests.head('https://httpbin.org/get')
print(r)

# HTTP OPTIONS Request
r = requests.options('https://httpbin.org/get')
print()



import requests
# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

# To pass a list of items as a value
payload = {'key1': 'value1', 'key2': ['value2','value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

# Response Content
r = requests.get('https://httpbin.org')
print(r.text)

# Binary Response Content
print(r.content)

# JSON Response Content
r = requests.get('https://api.github.com/events')
print(r.json())



# Custom Headers
import requests

url = 'https://httpbin.org'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r)

# More complicated POST Requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

payload_tuples = [('key1', 'value1'),('key1','value2')]
r1 =requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)

print(r1.text == r2.text)


import requests

# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)



import requests

# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/cookies')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)




# Timeouts
import requests

r=requests.get("https://httpbin.org", timeout=0.001)
print(r.text)

