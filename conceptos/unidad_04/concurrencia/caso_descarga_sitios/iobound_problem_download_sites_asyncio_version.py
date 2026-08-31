"""Version con asyncio para un problema limitado por entrada/salida de red."""

import asyncio
import time
from statistics import mean, stdev

import aiohttp


SITES = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 10
TIMEOUT_SECONDS = 10


async def download_site(session, url, verbose=True):
    async with session.get(url) as response:
        content = await response.read()
        if verbose:
            print(f"Read {len(content)} bytes from {url}")
        return len(content)


async def download_all_sites(sites, verbose=True):
    timeout = aiohttp.ClientTimeout(total=TIMEOUT_SECONDS)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [asyncio.create_task(download_site(session, url, verbose)) for url in sites]
        bytes_downloaded = await asyncio.gather(*tasks)
    return sum(bytes_downloaded)


def test_download_all_sites(sites, N=2):
    duration_times = []
    total_bytes = 0
    for _ in range(N):
        start_time = time.time()
        total_bytes = asyncio.run(download_all_sites(sites, verbose=False))
        duration_times.append(time.time() - start_time)
    return total_bytes, mean(duration_times), stdev(duration_times) if N > 1 else 0


if __name__ == "__main__":
    start_time = time.time()
    bytes_downloaded = asyncio.run(download_all_sites(SITES))
    duration = time.time() - start_time
    print(f"Downloaded {len(SITES)} sites and {bytes_downloaded} bytes in {duration:.3f} seconds")
