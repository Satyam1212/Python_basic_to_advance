
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as e:
        print(f"Please enter two numbers. Error: {e}")

print(sum("1", 2)) # 3