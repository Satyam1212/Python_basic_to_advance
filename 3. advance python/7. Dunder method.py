class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    # def __del__(self):
    #     print('deleted')

    def __call__(self):
        return 'yes'
    
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure.__str__()) # <__main__.Toy object at 0x7f8b1c3b3d30> # this is the default implementation of the dunder method __str__

print(str(action_figure)) # red # this is the implementation of the dunder method __str__ in the Toy class

print(len(action_figure)) # 5 # this is the implementation of the dunder method __len__ in the Toy class

# Dunder methods are special methods that python uses to execute some special operations behind the scenes

# del action_figure # deleted # this is the implementation of the dunder method __del__ in the Toy class  # this is commented out because it will give an error as the object is already deleted

print(action_figure()) # yes # this is the implementation of the dunder method __call__ in the Toy class 

print(action_figure['name']) # Yoyo # this is the implementation of the dunder method __getitem__ in the Toy class

