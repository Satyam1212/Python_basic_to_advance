def fib(number):
    a = 0
    b =1 
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

print(list(fib(1000))) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]