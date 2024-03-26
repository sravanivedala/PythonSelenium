'''
Created on 23-Mar-2024

@author: Rakesh
'''

def add(a,b):  # Function with parameters or arguments(formal arguments)
    c=a+b
    #print(c)
    return c
def sub(a,b):
    d=a-b
    #print(d)
    return d
'''
a=add(2,3) #actual arguments
print(a)
add(5,7)
'''
def add_sub(a,b):
    c=add(a,b)
    d=sub(a,b)
    return c,d
e,f=add_sub(2,3)
#print(e)
#print(f)
'''
def display():# calling function in the same function
    print("This is display function")
    display()
    
display()
 '''   