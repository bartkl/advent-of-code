import timeit
import functools


def time_performance(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        fn_output = fn(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"{fn.__qualname__} took {end_time - start_time:.6f} seconds.")

        return fn_output
    return wrapper


def pairwise(iterable):
    # NOTE: In Python 3.10 this is part of `itertools`.

    return zip(iter(iterable), iter(iterable[1:]))
