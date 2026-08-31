import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    # Aumentar estos valores si se quiere medir diferencias mas grandes.
    numbers = [2_000_000 + x for x in range(8)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration:.3f} seconds")
