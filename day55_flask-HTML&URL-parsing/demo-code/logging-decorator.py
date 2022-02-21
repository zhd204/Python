import functools


def logging_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        name = func.__name__
        if (not args) and (not kwargs):
            print(f"You called {name}({args}, {kwargs})")
        elif args and (not kwargs):
            print(f"You called {name}{args}")
        elif (not args) and kwargs:
            print(f"You called {name}{kwargs}")
        value = func(*args, **kwargs)
        print(f"It returned: {value}")

    return inner


@logging_decorator
def add_number1(a, b):
    return a + b


@logging_decorator
def add_number2(a, b, c=2):
    return a + b + c


add_number1(1, 2)

add_number2(1, 2, 3)