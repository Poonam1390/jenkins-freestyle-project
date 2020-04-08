import requests
api = 'http://localhost:5000'

print('HTTP POST Request (json):')
response = requests.post(api + '/post/json', json={"message": "mydata from the console or whereever this is"})
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' + str(response.json()["data"]))
