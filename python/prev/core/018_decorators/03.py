import time

def cache(func):
    cache_val = {}     # using dict instead of list makes things easier
    # print(cache_val) # initially this is empty

    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
         
        result = func(*args)
        cache_val[args] = result
        return result
    return wrapper        

@cache
def long_running_fuction(a, b):
    time.sleep(4)
    return a + b


print(long_running_fuction(2, 2))
print(long_running_fuction(2, 2))
print(long_running_fuction(1,2))



# notice the behaviour when you run the program