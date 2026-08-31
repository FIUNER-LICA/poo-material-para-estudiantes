import concurrent.futures
from time import sleep


counter = 0


def increment_counter(_):
    global counter
    for _ in range(100):
        current_value = counter
        sleep(0)  # Cede el control para facilitar que otro hilo interrumpa.
        counter = current_value + 1


if __name__ == "__main__":
    workers = 20
    expected = workers * 100

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(increment_counter, range(workers))

    print("El contador debería ser", expected, "y es", counter)
