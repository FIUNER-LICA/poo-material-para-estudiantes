def asynchronous():
    yield [1, 2, 3]
    # yield from [1, 2, 3]  # permite iterar sobre cada elemento del iterable


if __name__ == "__main__":
    gen = asynchronous()

    valores = next(gen)
    print(valores)
