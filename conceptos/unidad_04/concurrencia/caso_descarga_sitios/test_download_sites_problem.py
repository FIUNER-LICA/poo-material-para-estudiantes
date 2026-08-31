import iobound_problem_download_sites_asyncio_version as asyncio_version
import iobound_problem_download_sites_multiprocessing_version as multiprocessing_version
import iobound_problem_download_sites_non_concurrent as non_concurrent_version
import iobound_problem_download_sites_threading_version as threading_version


if __name__ == "__main__":
    sites = non_concurrent_version.SITES
    print("Problema descargar sitios", "en", len(sites), "descargas")

    N = 3
    methods = [
        ("non_concurrent", non_concurrent_version.test_download_all_sites),
        ("threading", threading_version.test_download_all_sites),
        ("asyncio", asyncio_version.test_download_all_sites),
        ("multiprocessing", multiprocessing_version.test_download_all_sites),
    ]

    print(
        "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Method", "Downloads", "Bytes", "Avg Time", "Std Deviation"
        )
    )
    for name, method in methods:
        total_bytes, t_m, t_std = method(sites, N)
        print(
            "{:<15} {:<15} {:<15} {:<15.3f} {:<15.3f}".format(
                name, len(sites), total_bytes, t_m, t_std
            )
        )
