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


# def once(val):
#     def _once(fn):
#         @functools.wraps(fn)
#         def wrapper(*args, **kwargs):
#             if not wrapper.has_run:
#                 fn_output = fn(*args, **kwargs)
#                 wrapper.has_run = True
#                 return fn_output
#             else:
#                 return val
#         wrapper.has_run = False
#         return wrapper
#     return _once

def cached_for_path(fn):
    @functools.wraps(fn)
    def wrapper(self, p):
        if p == (0, 0):
            wrapper.visited_points = set()

            fn_output = fn(self, p)
            return fn_output - wrapper.visited_points
        else:
            return set()
    wrapper.visited_points = set()
    return wrapper



def pairwise(iterable):
    # NOTE: In Python 3.10 this is part of `itertools`.

    return zip(iter(iterable), iter(iterable[1:]))
