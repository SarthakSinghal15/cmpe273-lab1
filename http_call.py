import requests
url = "https://webhook.site/b361e66d-cbfe-485d-bc88-790946eaf5e7"
response1=requests.get(url)
print(response1.headers['Date'])
response2=requests.get(url)
print(response2.headers['Date'])
response3=requests.get(url)
print(response3.headers['Date'])
