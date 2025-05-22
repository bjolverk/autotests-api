import httpx

# responce = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(responce.status_code)
# print(responce.json())
#
# data = {
#     'title': 'Новая задача',
#     'compleated': False,
#     'userId': 1
# }
#
# responce= httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(responce.status_code)
# print(responce.json())

# data= {"username": "test_user","password": "123456"}
#
# responce = httpx.post("https://httpbin.org/post", data= data)
# print(responce.json())

# headers = {"Authorization": "Bearer my_secret_token"}
#
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.json())  # Заголовки включены в ответ

# params = {"userId": 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response.url)
# print()
# print(response.json())

# files = {"file": ("example.txt", open("example.txt", "rb"))}
#
# response = httpx.post("https://httpbin.org/post", files=files, timeout=20)
#
# print(response.json())  # Ответ с данными о загруженном файле

# with httpx.Client() as client:
#     responce1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     responce2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(responce1.json())
# print(responce2.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
# except httpx.HTTPStatusError as err:
#     print(f"Ошибка запроса: {err}")
# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print("Запрос превысил лимит времени")