def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())

        if args_value is not '' and kwargs_value is not '':
            print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
        
    return wrapper







@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}!")

greet("chai", greeting="hanji")




# you can also add this decorator for some other functions without any argument

# eg:

@debug
def printHello():
    print("hello world!")

printHello()    