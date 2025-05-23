import httpx


from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

print('Create user data:', create_user_response_data)

login_payload = {
    'email': create_user_payload.get('email', 'Nope!'),
    'password': create_user_payload.get('password', 'Nope')
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('Login response data:', login_response_data)

authorization_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(
    f'http://localhost:8000/api/v1/users/{create_user_response_data.get('user').get('id')}',
    headers=authorization_user_headers

)
get_user_response_data = get_user_response.json()
print('Get user data:', get_user_response_data)

delete_user_response = httpx.delete(
    f'http://localhost:8000/api/v1/users/{create_user_response_data.get('user').get('id')}',
    headers=authorization_user_headers
)

print('Delete user status code:', delete_user_response.status_code)
