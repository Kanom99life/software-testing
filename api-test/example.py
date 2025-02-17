import requests

URL = "https://jsonplaceholder.typicode.com/posts"

data = {
    "userId": 1,
    "title": "salmon",
    "body": "ping river",
}

# response = requests.get(URL)
response = requests.post(URL, json=data)
assert response.status_code == 201

# print(response.status_code)
# print(response.text)
# print(response.json())
assert response.json()["id"] == 101 #check if id is 101
assert isinstance(response.json()["id"], int) #check if id is integer
# print(response.elapsed.total_seconds())
if "Content-Type" in response.headers:
    assert "application/json" in response.headers['Content-Type']