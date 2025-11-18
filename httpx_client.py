import httpx

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=1
)

response = client.get("api/v1/users/me")
print(response.json())