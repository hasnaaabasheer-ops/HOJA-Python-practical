def greet_decorator(func):
    def wrapper():
        print("before greeting...")
        func()
        print("after greeting...")
    return wrapper
@greet_decorator
def say_hello():
    print("Hello!")


say_hello()