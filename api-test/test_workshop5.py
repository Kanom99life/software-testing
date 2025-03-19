import requests
import pytest

@pytest.fixture
def api_client():
	session = requests.Session()
	yield session
	session.close()


# pytest -s
'''
Task 1
- Perform a GET request to https://api.zippopotam.us/us/90007
- Check that the response status code equals to 200
- Check that the value of the response header 'Content-Type' is 'application/json'
- Check that the response body element 'country' has a value equal to 'United States'
- Check that the response body element 'places' is a list and has a length of 1 (only one place corresponds to the US zip code 90007)
- Check that the first 'place name' element in the list of places has a value equal to 'Los Angeles'
'''
def test_task1(api_client):
	URL = 'https://api.zippopotam.us/us/90007'
	response = api_client.get(URL)
	assert response.status_code == 200
	if "Content-Type" in response.headers:
		assert "application/json" in response.headers['Content-Type']
	assert response.json()['country'] == 'United States'
	assert isinstance(response.json()['places'], list)
	assert len(response.json()['places']) == 1
	assert response.json()['places'][0]['place name'] == 'Los Angeles'







'''
Task 2
- Perform 10 GET requests to https://jsonplaceholder.typicode.com/posts
- Check that all response status codes equal to 200
- Check that, on average, the server responds less than 300 ms.
'''
def test_task2(api_client):
	avg = 0
	round = 10
	URL = 'https://jsonplaceholder.typicode.com/posts'
	for _ in range (round):
		response = api_client.get(URL)
		assert response.status_code == 200
		avg += response.elapsed.total_seconds()
	avg /= round
	assert avg < 0.3
	# print("avg = ", avg)








'''
Task 3
- Perform a GET request to https://jsonplaceholder.typicode.com/posts/1
- Check if the response code is 200
- Check if the response follows the expected JSON schema structure. 
- The schema should match the expected_schema format
DO NOT USE ANY EXTERNAL LIBRARIES
Hint: use isinstance(variable, type) function for this
'''
def test_task3(api_client):
	expected_schema = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }
	URL = 'https://jsonplaceholder.typicode.com/posts/1'
	response = api_client.get(URL)
	assert response.status_code == 200
	for key in expected_schema:
		assert key in response.json()
		assert isinstance(response.json()[key], expected_schema[key])








'''
Task 4
- Perform a PATCH update to https://jsonplaceholder.typicode.com/users/1
to change the email of the user id 1 to "cs364@cs.science.cmu.ac.th"
- Check that response status code is okay (200)
- Check that the returned data shows the new email for the user.
'''
def test_task4(api_client):
	URL = 'https://jsonplaceholder.typicode.com/users/1'
	data = {
		'email': 'cs364@cs.science.cmu.ac.th',
	}

	patch_data = api_client.patch(URL, json=data)
	assert patch_data.status_code == 200 and patch_data.json()['email'] == "cs364@cs.science.cmu.ac.th"
	# assert patch_data.json()['email'] == "cs364@cs.science.cmu.ac.th"
	# print(patch_data.json())
	# print(patch_data.text)
	# print("Updated email = ",patch_data.json()['email'])








'''
Task 5
- Use the username and password from https://dummyjson.com/users (any user)
- Perform a POST request to https://dummyjson.com/auth/login 
and pass the username and password object to the request
- Check that the response status code is okay
- Check that the server sends 'accessToken' back
- Perform a GET request with Authorization header with accessToken above to https://dummyjson.com/auth/me
- Check that the response code is 200
- Check that the returned user is the correct one (check if usernames are the same).
- Perform the same request but with incorrect accessToken
- Check that the response code is 401 (unauthorized) and the response's json object 'message' field says "Invalid/Expired Token!"
'''
def test_task5(api_client):
	#Get username and password
	USER_URL = 'https://dummyjson.com/users'
	response = api_client.get(USER_URL)
	get_username = response.json()["users"][0]["username"]
	get_password = response.json()["users"][0]["password"]
	
	#Login
	data = {
		'username': get_username,
		'password': get_password,
	}
	LOGIN_URL = 'https://dummyjson.com/auth/login'
	login_api = api_client.post(LOGIN_URL, json=data)
	assert login_api.status_code == 200
	if "accessToken" in login_api.json():
		assert "accessToken" in login_api.json()
	
	accessToken = login_api.json()["accessToken"]
	# print("accessToken = ", accessToken)

	#Check about me
	ABOUTME_URL = 'https://dummyjson.com/auth/me'
	me = api_client.get(ABOUTME_URL, headers={'Authorization': f'Bearer {accessToken}'})
	assert me.status_code == 200
	assert me.json()["username"] == get_username
	# print(me.json())	

	incorrect_accessToken = "12345"
	incorrect_me = api_client.get(ABOUTME_URL, headers={'Authorization': f'Bearer {incorrect_accessToken}'})
	
	assert incorrect_me.status_code == 401 and incorrect_me.json()["message"] == "Invalid/Expired Token!"
	








