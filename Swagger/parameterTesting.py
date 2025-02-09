
import requests

para = {
    'page' : 3,
    'per_page' : 2
}

url = 'https://gorest.co.in/public/v2/users'
para_response = requests.get(url=url,params=para)

print(para_response.json())

assert para_response.status_code == 200