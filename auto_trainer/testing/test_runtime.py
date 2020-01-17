import time
import statistics as stat


def get_avg_runtime(method, num_samples=10):
    runtimes = []
    for _ in range(num_samples):
        start_time = time.time()
        method()
        runtimes.append((time.time() - start_time))
    return stat.mean(runtimes)
