# *args **kwargs

# def super_func(args):
#     return sum(args)

# print(super_func(1,2,3,4,5)) # TypeError: super_func() takes 1 positional argument but 5 were given

# To solve this we can use *args
def super_func(name, *args, **kwargs):
    print(args) # (1, 2, 3, 4, 5)
    print(kwargs) # {'num1': 5, 'num2': 10}
    return sum(args) + sum(kwargs.values())

print(super_func('andy',1,2,3,4,5, num1=5, num2=10)) # 15

# Rule: params, *args, default parameters, **kwargs