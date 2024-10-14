picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='') # end='' is used to print in the same line
        else:
            print(' ', end='')
    print('')

# What is good code?
# clean (readable, understandable, maintainable)
# predictability
# DRY (Don't Repeat Yourself)