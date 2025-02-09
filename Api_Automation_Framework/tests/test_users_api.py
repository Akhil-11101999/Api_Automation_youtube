import pytest
# from utils.api_client import APIClient
from api_client import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    # data = response.json()
    # print(data[1]['name'])
    assert response.status_code == 200
    assert len(response.json()) > 0
    # assert data[1]['name'] == 'Ervin Howell'


def test_create_users(api_client,load_user_data):
    # user_data = {
    #     'name':'harsha',
    #     'username':'qa tester',
    #     'email':'apitesting@gmail.com'
    # }
    user_data = load_user_data['new_user']
    uniq_email = f'{uuid.uuid4().hex[:8]}@gmail.com'
    print(uniq_email)
    user_data['email'] = uniq_email
    response = api_client.post("users",user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'harsha'
    id = response.json()['id']
    response_get = api_client.get("users/10")
    print(response_get.json())
    assert response_get.status_code == 200
    assert response_get.json()['name'] == 'Clementina DuBuque'


def test_update_users(api_client):
    user_data = {
            'name': 'harsha 123',
            'username': 'qa 234',
            'email': 'apitesting@gmail.com'
        }
    response = api_client.put("users/2",user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'harsha 123'

def test_delete_users(api_client):
    response=api_client.delete("users/2")
    print(response.json())
    assert response.status_code == 200



# def test_create_users(api_client,load_user_data):
#     # user_data = {
#     #     "name": "prasanth",
#     #     "username":"qa user",
#     #     "email":"test@gmail.com"
#     # }
# #hi hello prasanth
#     user_data = load_user_data["new_user"]
#
#     unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
#     print(unique_email)
#     user_data["email"] = unique_email
#
#     response = api_client.post("users", user_data)
#     print(response.json())
#     assert response.status_code == 201
#     assert response.json()['name'] == 'prasanth'
#     id = response.json()['id']
#     responseget = api_client.get("users/10")
#     print(responseget.json())
#     assert responseget.status_code == 200
#     assert responseget.json()['name'] == 'Clementina DuBuque'
#
#
# def test_update_users(api_client):
#     user_data = {
#         "name": "prasanth k",
#         "username":"qa user",
#         "email":"test@gmail.com"
#     }
#     response = api_client.put("users/1", user_data)
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json()['name'] == 'prasanth k'
#
#
# def test_delete_users(api_client):
#     response = api_client.delete("users/1")
#     print(response.json())
#     assert response.status_code == 200