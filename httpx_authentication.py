import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login response:', login_response_data)
print('Status code:', login_response.status_code)

refresh_payload = {
    "refreshToken": login_response_data.get('token', 'Nope').get('accessToken', 'Nope')
}
# print(refresh_payload)
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print('Login response:', refresh_response_data)
print('Status code:', refresh_response.status_code)
