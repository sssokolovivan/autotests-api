import httpx
from tools.fakers import get_random_email

BASE_URL = "http://localhost:8000"

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(f"{BASE_URL}/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response.json()['user']['id']

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post(f"{BASE_URL}/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

patch_payload = {
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

patch_user_response = httpx.patch(f"{BASE_URL}/api/v1/users/{user_id}", headers=headers, json=patch_payload)
patch_user_response_data = patch_user_response.json()

print("Статус код для запроса на создание нового объекта:", create_user_response.status_code)
print("Статус код для запроса на авторизацию:", login_response.status_code)
print("Статус код для запроса на обновление объекта:", patch_user_response.status_code)