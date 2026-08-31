import multiprocessing
import sys
import time
from pathlib import Path
from statistics import mean, stdev

sys.path.append(str(Path(__file__).resolve().parents[1]))
import load_data as ld  # noqa: E402


DATA_DIR = Path(__file__).resolve().parent / "datos_ejemplo"


def count_words(filename, encoding="utf-8", delay_seconds=0):
    """Funcion de trabajo: debe estar a nivel de modulo para multiprocessing."""
    if delay_seconds:
        time.sleep(delay_seconds)
    with open(filename, "r", encoding=encoding) as file:
        return len(file.read().split())


def count_words_in_all_files(filenames, delay_seconds=0):
    with multiprocessing.Pool() as pool:
        words = pool.starmap(count_words, [(filename, "utf-8", delay_seconds) for filename in filenames])
    return sum(words)


def test_count_words_in_all_files(filenames, N=2, delay_seconds=0):
    duration_times = []
    words = 0
    for _ in range(N):
        start_time = time.time()
        words = count_words_in_all_files(filenames, delay_seconds)
        duration_times.append(time.time() - start_time)
    return words, mean(duration_times), stdev(duration_times) if N > 1 else 0


if __name__ == "__main__":
    paths = [DATA_DIR]
    filenames = ld.load_filenames(paths)

    words, t_m, t_std = test_count_words_in_all_files(filenames)
    print(f"{words} palabras en {len(filenames)} archivos en {t_m:.3f} segundos")
