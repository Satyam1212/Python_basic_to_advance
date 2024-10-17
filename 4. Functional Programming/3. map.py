# map(action, data)

def multiply_by2(li):
    # Write now we are using map function so we don't need to create new_list and append item*2 in it.
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return li*2

print(list(map(multiply_by2, [1,2,3]))) # [2, 4, 6]
print(list(map(multiply_by2, [1,2,3,4,5]))) # [2, 4, 6, 8, 10]