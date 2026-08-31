from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
import load_data as ld  # noqa: E402

import iobound_problem_count_words_txtfiles_asyncio as asyncio_version
import iobound_problem_count_words_txtfiles_multiprocessing as multiprocessing_version
import iobound_problem_count_words_txtfiles_non_concurrent as non_concurrent_version
import iobound_problem_count_words_txtfiles_threading as threading_version


if __name__ == "__main__":
    paths = [Path(__file__).resolve().parent / "datos_ejemplo"]
    filenames = ld.load_filenames(paths) * 100
    print("Problema contar palabras", "en", len(filenames), "archivos")

    # Se repiten rutas chicas para tener muchas tareas sin agregar archivos al repo.
    # La pausa se define aca para no mezclar la simulacion con los ejemplos base.
    N = 3
    simulated_io_delay_seconds = 0.01
    methods = [
        ("non_concurrent", non_concurrent_version.test_count_words_in_all_files),
        ("threading", threading_version.test_count_words_in_all_files),
        ("asyncio", asyncio_version.test_count_words_in_all_files),
        ("multiprocessing", multiprocessing_version.test_count_words_in_all_files),
    ]

    print("{:<15} {:<15} {:<15} {:<15}".format("Method", "Num. Words", "Avg Time", "Std Deviation"))
    for name, method in methods:
        words, t_m, t_std = method(filenames, N, simulated_io_delay_seconds)
        print("{:<15} {:<15} {:<15.3f} {:<15.3f}".format(name, words, t_m, t_std))
