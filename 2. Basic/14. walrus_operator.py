a = 'hellooooooooooooooooo'

if ((n := len(a) > 10)):
    print(f'{n} too long {len(a)} elements') # True too long 21 elements

while (n := len(a) > 1):
    print(n)
    a = a[:-1] 