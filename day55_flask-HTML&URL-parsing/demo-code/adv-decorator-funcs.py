import functools


def is_authenticated_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if args[0].is_logged_in:
            func(*args, **kwargs)
        else:
            print("Not authenticated!")

    return inner


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    @is_authenticated_decorator
    def create_blog_post(self):
        print(f"This is {self.name}'s new blog post.")


new_user = User("Tom")
new_user.create_blog_post()
print("---------------------")
new_user.is_logged_in = True
new_user.create_blog_post()
