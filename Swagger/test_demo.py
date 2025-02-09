import pytest
import requests

def test_Getrequest_validation():

    head = {
        'Content-type': 'Application/json'
    }

    base_url = 'https://reqres.in/'
    response = requests.get(base_url+'api/users/2',headers=head)

    assert response.status_code == 200
    print(response.text)