import queue
import random
import time

queue_requests = queue.Queue()

def generate_request():
    request = random.randint(1, 50)
    print(f"Створено заяку: {request}")
    queue_requests.put(request)

def process_request():
    if not queue_requests.empty():
        request = queue_requests.get()
        print(f"Обробка заявки: {request}")
    else:
        print("Черга є пустою")

try:
    while True:
        generate_request()
        process_request()
        time.sleep(2)

except KeyboardInterrupt:
    print("Програму зупинено користувачем.") # Вихід при натисканні Ctrl + C для користувачів Windows, та Control + C для macOS
except Exception as e:
    print(f"Виникла помилка: {e}")
    