from execnet import loads
from requests import Session
from json import loads

base_url = "https://www.shoppersstack.com/shopping"

session  = Session()
session.headers.update({"Content-Type": "application/json"})
paylod = {
  "email": "akhil.11101999@gmail.com",
  "password": "Akhil@123",
  "role": "SHOPPER"
}
response = session.post(f"{base_url}/users/login",json=paylod)
assert response.status_code == 200 ,"test case faild"
print("test case pass")

body = loads(response.text)
shopper_id = body["data"]["userId"]
bearer_token = body["data"]["jwtToken"]
res = session.get(f"{base_url}/products/alpha")
assert res.status_code == 200,"test case falild"

print("test case pass")
res_body = loads(res.text)
productId = res_body["data"][0]["productId"]
print(productId)

session.headers.update({"Authorization":f"Bearer {bearer_token}"})
get_res = session.get(f"{base_url}/shoppers/{shopper_id}/wishlist")
assert get_res.status_code == 200,f"test fail {get_res.status_code}"
print("test pass")



