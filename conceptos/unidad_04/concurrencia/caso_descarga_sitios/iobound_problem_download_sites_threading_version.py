"""Version con hilos para un problema limitado por entrada/salida de red."""

import concurrent.futures
import threading
import time
from statistics import mean, stdev

import requests


SITES = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 10
TIMEOUT_SECONDS = 10
thread_local = threading.local()


def get_session():
    # Cada hilo conserva su propia Session; una misma Session no es thread-safe.
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url, verbose=True):
    session = get_session()
    with session.get(url, timeout=TIMEOUT_SECONDS) as response:
        content_length = len(response.content)
        if verbose:
            print(f"Read {content_length} bytes from {url}")
        return content_length


def download_all_sites(sites, verbose=True):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        bytes_downloaded = executor.map(download_site, sites, [verbose] * len(sites))
    return sum(bytes_downloaded)


def test_download_all_sites(sites, N=2):
    duration_times = []
    total_bytes = 0
    for _ in range(N):
        start_time = time.time()
        total_bytes = download_all_sites(sites, verbose=False)
        duration_times.append(time.time() - start_time)
    return total_bytes, mean(duration_times), stdev(duration_times) if N > 1 else 0


if __name__ == "__main__":
    start_time = time.time()
    bytes_downloaded = download_all_sites(SITES)
    duration = time.time() - start_time
    print(f"Downloaded {len(SITES)} sites and {bytes_downloaded} bytes in {duration:.3f} seconds")
