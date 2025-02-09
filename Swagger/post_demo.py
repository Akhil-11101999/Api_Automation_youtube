import requests
import json


head = {
    'Content-type' :'Application/json'
}

# json_file = open('users.json')
with open('users.json') as json_file:
    json_pyaload = json.load(json_file)

base_url = 'https://reqres.in/api/users'

response = requests.post(url=base_url, headers=head ,json=json_pyaload)


data = response.json()
print(data['name'])
print(response.status_code)
print(response.text)
