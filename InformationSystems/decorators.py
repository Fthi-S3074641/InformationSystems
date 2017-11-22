import time


def measure_performance(num_queries):
    def wrap(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            print(f"Performance of {func.__name__}: {(t2 - t1)/num_queries}s")

        return wrapper

    return wrap
