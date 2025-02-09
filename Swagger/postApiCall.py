
import  requests

header = {
    "Accept":"text/plain",
    "Content-Type":"application/json"
}

payload = {
    "id": 145,
    "title": "learning api testing",
    "dueDate": "2025-02-02T02:24:18.563Z",
    "completed": False
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities"
        ,headers=header , json=payload )

print(response.status_code)
print(response.json())

data = response.json()

assert data['id'] == 145
assert data['title'] == 'learning api testing'
assert response.status_code == 200