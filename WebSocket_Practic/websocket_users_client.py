import asyncio

import websockets

async def recieve_messages(websocket):
    try:
        print('Введите сообщение: ')
        async for message in websocket:
            print(f"[Сервер]: {message}")
    except websockets.exceptions.ConnectionClosed:
        print('Соединение разорвано')

async def send_messages(websocket):
    try:
        while True:
            message = await asyncio.get_event_loop().run_in_executor(None, input,)
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print('Соединение разорвано')

async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        print('Подключение к серверу...')
        await asyncio.gather(
            recieve_messages(websocket),
            send_messages(websocket)
        )

asyncio.run(client())