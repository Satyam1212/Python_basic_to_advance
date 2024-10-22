
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
    for i in range(100000):
        i*5

long_time() # Nothing happen

# Like this you can use the performance decorator to measure the time taken by any function to execute.

# Similarly for login_required decorator, you can use it to restrict access to certain functions in your application.

# You can also use the @login_required decorator to restrict access to certain functions in your application.