#MRO - Method Resolution Order - It is the order in which the classes are searched in object oriented programming languages to execute a method.

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num) # 1
# In the above example, the num attribute of the class C is printed because the class C is the first class in the MRO of class D.

print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]

# for MRO they use depth first search algorithm

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

print(M.mro()) # [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]