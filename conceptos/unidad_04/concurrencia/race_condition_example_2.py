import threading
from time import sleep


x = 0
REPETICIONES = 1_000


def increment():
    global x
    for _ in range(REPETICIONES):
        current_value = x
        sleep(0)
        x = current_value + 1


def decrement():
    global x
    for _ in range(REPETICIONES):
        current_value = x
        sleep(0)
        x = current_value - 1


threads = []
for _ in range(10):  # Ejecutar el codigo 10 veces simultaneamente.
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=decrement)
    threads.append(thread1)
    threads.append(thread2)
    thread1.start()
    thread2.start()

for thread in threads:
    thread.join()

print("Valor esperado de x:", 0)
print("Valor final de x:", x)  # Puede variar por la race condition.
