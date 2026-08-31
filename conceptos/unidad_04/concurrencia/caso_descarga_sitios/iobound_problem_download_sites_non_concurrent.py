"""Version secuencial del problema de descarga de sitios."""

import time
from statistics import mean, stdev

import requests


SITES = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 10
TIMEOUT_SECONDS = 10


def download_site(url, session, verbose=True):
    with session.get(url, timeout=TIMEOUT_SECONDS) as response:
        content_length = len(response.content)
        if verbose:
            print(f"Read {content_length} bytes from {url}")
        return content_length


def download_all_sites(sites, verbose=True):
    total_bytes = 0
    with requests.Session() as session:
        for url in sites:
            total_bytes += download_site(url, session, verbose)
    return total_bytes


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
