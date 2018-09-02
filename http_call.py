import requests
url = "https://webhook.site/b361e66d-cbfe-485d-bc88-790946eaf5e7"
responses = []
for i in range(3):
    responses.append(requests.get(url).headers['Date'])
for response in responses:
    print(response) 
