import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(fn):
    def inner_func():
        start = time.time()
        fn()
        end = time.time()
        print(f"{fn.__name__} speed: {end - start} s")

    return inner_func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
