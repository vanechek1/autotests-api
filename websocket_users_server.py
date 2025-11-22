import asyncio

import websockets
from websockets import ServerConnection


async def send_messages(websocket, message):
    print(f'Сообщение от пользователя: {message}')
    response = f'Сообщение пользователя: {message}'
    for _ in range(5):
        await websocket.send(response)
        await asyncio.sleep(2)

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f'Получено сообщение от пользователя: {message}')
        asyncio.create_task(send_messages(websocket, message))

async def main():
    server = await websockets.serve(echo, 'localhost', 8765)
    print(f'Сервер запущен на ws://localhost:8765')
    await server.wait_closed()

asyncio.run(main())