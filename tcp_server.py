import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET - сокет будет идти по ipv4. SOCK_STREAM - TCP соединение

    server_address = ('localhost', 12345)
    server_socket.bind(server_address) # Привязываем сокет к нашему адресу

    server_socket.listen(5) # Принимает не более 5 соединений (6ой будет в очереди)
    print('Сервер запущен и ждет подключений...')

    while True:
        client_socket, client_address = server_socket.accept() # Принимаем подключение клиента
        print(f'Подключение от {client_address}')

        data = client_socket.recv(1024).decode() # Ждет данных от клиента (могут быть отправлены не сразу)
        print(f'Получено сообщение: {data}')

        response = f'Сервер получил: {data}'
        client_socket.send(response.encode()) # Отправляем в байтовом представлении

        client_socket.close()

if __name__ == '__main__':
    server()