import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
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

patch_user_payload = {
    "email": fake.email(),
    "password": "123456QWERTY",
    "lastName": "Sharikov",
    "firstName": "Polygraph",
    "middleName": "111"
}
update_user_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{create_user_response_data.get('user').get('id')}',
    json=patch_user_payload,
    headers=authorization_user_headers
)
update_user_response_data = update_user_response.json()

print('Update user data:', update_user_response_data)

# На всякий случай, проверяем:
# get_user_response = httpx.get(
#     f'http://localhost:8000/api/v1/users/{create_user_response_data.get('user').get('id')}',
#     headers=authorization_user_headers
#
# )
# get_user_response_data = get_user_response.json()
#
#
# assert get_user_response_data == update_user_response_data
#
# delete_user_response = httpx.delete(
#     f'http://localhost:8000/api/v1/users/{create_user_response_data.get('user').get('id')}',
#     headers=authorization_user_headers
# )
#
# print('Delete user status code:', delete_user_response.status_code)