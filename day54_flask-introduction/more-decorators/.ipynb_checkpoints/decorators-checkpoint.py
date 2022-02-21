def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        d = func(*args, **kwargs)
        return d
        
    return wrapper_do_twice

