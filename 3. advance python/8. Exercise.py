class SuperList(list):
    def __len__(self):
        return 1000
    

super_list1 = SuperList()
print(len(super_list1)) # 1000

super_list1.append(5) # AttributeError: 'SuperList' object has no attribute 'append' so we can see that the SuperList class is not inheriting from the list class so we need to inherit from the list class to use the append method

super_list1.extend([1, 2, 3])

print(super_list1) # [1, 2, 3] so we can see that the SuperList class is not inheriting from the list class so we need to inherit from the list class to use the extend method

print(issubclass(SuperList, list)) # True