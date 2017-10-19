from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print('I started')
        func(*args, **kwargs)
        print('I\'m done!')
    return wrapped

@my_decorator
def func():
    print('I\'m a function')
func()

def my_class_decorator(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        func(user='Admin321', email='admin@admin.com', *args, **kwargs)

    return wrapped

class Class:
    @my_class_decorator
    def email(user, email):
        print(f'Hello {user}, your email is {email}!')
x = Class()
x.email()
