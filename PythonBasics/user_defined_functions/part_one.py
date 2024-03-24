'''
Created on 23-Mar-2024

@author: Rakesh
'''
'''
def add(a,b):  # Function with parameters or arguments(formal arguments)
    c=a+b
    print(c)
    return c

a=add(2,3) #actual arguments
print(a)
add(5,7)
'''
def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d
e,f=add_sub(2,3)
print(e)
print(f)