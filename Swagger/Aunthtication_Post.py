import requests

head = {
    'content-Type':'Application/json',
    'authorization':'Bearer 3e740ef5ef40cbe993187bbe701f43a447f961e9946dd9570f6adc4b9a11fcc7'
}

body = {
    "name": "Akhil",
    "email": "apitesting5@gmail.com",
    "gender": "male",
    "status": "active"
  }

url = 'https://gorest.co.in/public/v2/users'

Auth_response = requests.post(url,headers=head,json=body)

print('frst create data')
print(Auth_response.json())

assert Auth_response.status_code == 201


get_response = requests.get(url+'/'+str(Auth_response.json()['id']),headers=head)

print('fetch data by adding id in url')
print(get_response.json())

assert get_response.status_code == 200