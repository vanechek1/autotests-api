import time

counter = 0
def get_random_email() -> str:
    global counter
    counter += 1
    return f'test.{time.time()}.{counter}@example.com'