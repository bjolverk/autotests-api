import httpx

login_payload = {
    "email": "new_bjolverk@example.com",
    "password": "123456789QAZ"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload, timeout=20)
login_response_data = login_response.json()

print('Login response:', login_response_data)
print('Status code:', login_response.status_code)

acc_token = login_response_data.get('token', 'Nope!').get('accessToken', 'Nope!')
headers = {"Authorization": f"Bearer {acc_token}"}
me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
me_response_data = me_response.json()

print('users response:', me_response_data)
print('Status code:', me_response.status_code)