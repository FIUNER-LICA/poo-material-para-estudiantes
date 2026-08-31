import asyncio
import sys
import time
from pathlib import Path
from statistics import mean, stdev

sys.path.append(str(Path(__file__).resolve().parents[1]))
import load_data as ld  # noqa: E402


DATA_DIR = Path(__file__).resolve().parent / "datos_ejemplo"


def count_words_sync(filename, encoding="utf-8", delay_seconds=0):
    if delay_seconds:
        time.sleep(delay_seconds)
    with open(filename, "r", encoding=encoding) as file:
        return len(file.read().split())


async def count_words(filename, encoding="utf-8", delay_seconds=0):
    """asyncio no vuelve asincronico al disco; delegamos la lectura a un hilo."""
    return await asyncio.to_thread(count_words_sync, filename, encoding, delay_seconds)


async def count_words_in_all_files(filenames, delay_seconds=0):
    tasks = [
        asyncio.create_task(count_words(filename, delay_seconds=delay_seconds))
        for filename in filenames
    ]
    words = await asyncio.gather(*tasks)
    return sum(words)


def test_count_words_in_all_files(filenames, N=2, delay_seconds=0):
    duration_times = []
    words = 0
    for _ in range(N):
        start_time = time.time()
        words = asyncio.run(count_words_in_all_files(filenames, delay_seconds))
        duration_times.append(time.time() - start_time)
    return words, mean(duration_times), stdev(duration_times) if N > 1 else 0


if __name__ == "__main__":
    paths = [DATA_DIR]
    filenames = ld.load_filenames(paths)
    words, t_m, t_std = test_count_words_in_all_files(filenames)
    print(f"{words} palabras en {len(filenames)} archivos en {t_m:.3f} segundos")
