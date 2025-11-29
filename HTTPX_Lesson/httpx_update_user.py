import httpx

from tools.fakers import get_random_email

create_user_response = None
login_response = None
update_response = None
create_user_response_data = None
login_response_data = None
update_response_data = None

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

try:
    with httpx.Client() as client:
        create_user_response = client.post('http://localhost:8000/api/v1/users', json=create_user_payload)
        create_user_response.raise_for_status()
        create_user_response_data = create_user_response.json()

        login_response = client.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
        login_response.raise_for_status()
        login_response_data = login_response.json()

        headers = {
            "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
        }

        update_response = client.patch(f'http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}',
                                       headers=headers,
                                       json=update_user_payload
                                       )
        update_response.raise_for_status()
        update_response_data = update_response.json()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
except httpx.RequestError as e:
    print(f"Ошибка подключения: {e}")
except KeyError as e:
    print(f'Ошибка аутентификации. Отсутствует: {e}')

print('=== Результаты выполнения программы ===')

if create_user_response and create_user_response_data:
    print("Create user status code: ", create_user_response.status_code)
    print("Create user response: ", create_user_response_data)
else:
    print('Создание юзера не было выполнено')

if login_response and login_response_data:
    print("Login status code: ", login_response.status_code)
    print("Login response data: ", login_response_data)
else:
    print('Авторизация не была выполнена')

if update_response and update_response_data:
    print("Update user status code: ", update_response.status_code)
    print("Update user response: ", update_response_data)
else:
    print('Обновление юзера не было выполнено')