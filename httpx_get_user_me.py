import httpx

payload = {
  "email": "test_user@gg.gg",
  "password": "pass1234",
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
access_token = login_response.json()["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)


print(response.json())
print(response.status_code)