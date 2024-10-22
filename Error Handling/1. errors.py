# print(1+True) # 2

# print(1+"hello") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Error Handling
# Error handling is the process of catching errors in your code and taking appropriate action.

# def hooohoo()
#     pass # SyntaxError: invalid syntax

# The above code will raise a SyntaxError because of the missing colon at the end of the function definition.

while True:        
    try:
        age = int(input('Enter your age: '))
        10/age # this should give error if age is 0
        print(age)
        raise ValueError('Hey cut it out!')
    # except ValueError:
    #     print('Please enter a valid number') 
    #     continue
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
        break
    else:
        print('Thank you!')
        break
    finally:
        print('Ok, I am finally done!')
    print('Can you hear me?') # This line will never be executed
    
# print(age) # ValueError: invalid literal for int() with base 10: 'twenty'