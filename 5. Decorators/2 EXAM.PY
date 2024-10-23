
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time() # Start time
        result = fn(*args, **kwargs)
        t2 = time() # End time
        print(f'It took {t2-t1} ms')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5

long_time() # It took 0.006069183349609375 ms
long_time2() # It took 0.008994102478027344 ms

# Like this you can use the performance decorator to measure the time taken by any function to execute.

# Similarly for login_required decorator, you can use it to restrict access to certain functions in your application.

# You can also use the @login_required decorator to restrict access to certain functions in your application.