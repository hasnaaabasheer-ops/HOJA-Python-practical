def greet_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper
@greet_decorator
def greet():
    print("Hello")

greet()