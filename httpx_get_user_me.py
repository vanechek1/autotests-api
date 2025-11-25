import httpx
import json
import sys

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

try:
    login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload, timeout=20)
    login_response.raise_for_status()

    login_response_data = login_response.json()
    print(login_response_data)
    print(f'Статус код: {login_response.status_code}')

    accessToken = login_response_data['token']['accessToken']
    headers = {
        'Authorization': f'Bearer {accessToken}'
    }
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса {e}')
    sys.exit(1)
except KeyError as e:
    print(f'Ошибка аутентификации. Отсутствует: {e}')  # в случае, если ошибка на этапе парсинга accessToken
    sys.exit(1)

try:
    user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
    user_response.raise_for_status()

    user_response_data = user_response.json()
    print(user_response_data)
    print(f'Статус код: {user_response.status_code}')

    print('Другой формат вывода:')
    print(json.dumps(user_response.json(), indent=4))
except httpx.HTTPStatusError as e:
    print(f'Ошибка запросе {e}')

# === Реализация с помощью контекстного менеджера ===
# with httpx.Client() as client:
#     try:
#         login_response = client.post('http://localhost:8000/api/v1/authentication/login', json=login_payload, timeout=20)
#         login_response.raise_for_status()
#
#         login_response_data = login_response.json()
#         print(login_response_data)
#         print(f'Статус код: {login_response.status_code}')
#
#         accessToken = login_response_data['token']['accessToken']
#         headers = {
#             'Authorization': f'Bearer {accessToken}'
#         }
#     except httpx.HTTPStatusError as e:
#         print(f'Ошибка запроса {e}')
#         sys.exit(1)
#     except KeyError as e:
#         print(f'Ошибка аутентификации. Отсутствует: {e}')  # в случае, если ошибка на этапе парсинга accessToken
#         sys.exit(1)
#
#     try:
#         user_response = client.get('http://localhost:8000/api/v1/users/me', headers=headers)
#         user_response.raise_for_status()
#
#         user_response_data = user_response.json()
#         print(user_response_data)
#         print(f'Статус код: {user_response.status_code}')
#
#         print('Другой формат вывода:')
#         print(json.dumps(user_response.json(), indent=4))
#     except httpx.HTTPStatusError as e:
#         print(f'Ошибка запросе {e}')
