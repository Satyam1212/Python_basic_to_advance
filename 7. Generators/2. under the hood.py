def special_for(iterable):
    iterator = iter (iterable) # iter() is a built-in function that returns an iterator object which can be iterated one element at a time and allows us to use the next() method to get the next element.
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])