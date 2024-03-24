'''
Created on 10-Mar-2024

@author: Rakesh
'''
import sys
a=2 # int # hard-coded values(values given in program itself)
b=3.5  # float
c=6+8j  # complex
d= "dog" # str
e=True # boolean
f=False # boolean
g=None #NoneType  used as place holder or when functions return nothing
print("a", type(a))
print(sys.getsizeof(a))
print("b", type(b))
print(sys.getsizeof(b))
print("c", type(c))
print(sys.getsizeof(c))
print("d", type(d))
print(sys.getsizeof(d))
print("e=", type(e))
print(sys.getsizeof(e))
print("f", type(f))
print(sys.getsizeof(f))
print("g", type(g))
print(sys.getsizeof(g))