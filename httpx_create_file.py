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

create_file_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
create_file_response = httpx.post(
    'http://localhost:8000/api/v1/files',
    data={'filename': 'image.png', 'directory': 'courses'},
    files={'upload_file': open('./testdata/files/image.png', 'rb')},
    headers=create_file_header
)
create_file_response_data  = create_file_response.json()
print('Create file data:', create_file_response_data)