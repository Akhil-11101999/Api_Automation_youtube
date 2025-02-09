import requests

head ={
    "Accept":"text/plain"
}
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5",headers=head)
print("Before Update")
print(response.json())

put_head = {
    "Accept" : "text/plain",
    "Content-Type" : "application/json"
}

put_payload = {
  "id": 10,
  "title": "im changing/Updating ID",
  "dueDate": "2025-02-02T03:36:01.436Z",
  "completed": True
}

response_put = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/5",
                            headers=put_head,json=put_payload) # both url is same

print("After Update")
print(response_put.json())