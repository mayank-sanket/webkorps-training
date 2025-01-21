import time
import math

def timer(func):
    def wrapper(*args, **kwargs):   # **kwargs is optional here
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {math.floor((end - start))} seconds.")
        return result
        
    return wrapper

@timer   # this decorator makes the example_function pass through the timer function when the example_function is called
def example_function(n):
    time.sleep(n)

example_function(2)    