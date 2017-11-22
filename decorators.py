import time


def measure_performance():
    def wrapper(func):
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"Performance of {func.__name__}: {t2 - t1}s")

    return wrapper
