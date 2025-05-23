# from mimesis import Person

import httpx
from tools.fakers import get_random_email
#
# my_person = Person('ru')
# print(my_person.email())
# print(my_person.full_name())
# print(my_person.first_name())
# print(my_person.last_name())
# print(my_person.username())
# print(my_person.password())
# print(my_person.surname())

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
print(response.status_code)
print(response.json())