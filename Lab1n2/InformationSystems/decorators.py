import time

from functools import wraps


def measure_total_time(num_queries):
    def wrap(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            res = func(*args, **kwargs)
            t2 = time.time()
            mod = "Average " if num_queries > 1 else ""
            print(f"{mod}Performance of {func.__name__}: {(t2 - t1)/num_queries}s")
            return res

        return wrapper

    return wrap
