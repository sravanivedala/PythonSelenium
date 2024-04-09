'''
Polymorphism
poly:Many
Morph:forms

1. Overloading:
    a. Operator overloading
        + --> arithmetic addition of 2 numerical data types
          --> combining 2 strings
          --> extending the list with elements of another list
    b. Method overloading: Having methods with same name but different no. of parameters in the same class. but python does not support methods with same name in a class
            (we tried with @overload decorator imported as shown in built-ins but it didn't work)
            we can implement method overloading by using variable length arguments
            & method overloading using default values
    c. Constructor overloading: we can implement constructor overloading by using variable length arguments
            & constructor overloading using default values
    
2. Over-riding:
    
    a. Method over-riding
    b. Constructor Over-riding

'''
#from typing import overload
'''
#operator overloading

print(2+4.9)
print("2"+"4.9")
print([1,2,3,4] +[5,6,7,8])
'''

#Method overloading
'''
class Example:
    def method_one(self):
        print("This is method without parameters")
    @overload 
    def method_one(self,a):
        print(f"This is method with one parameter {a}" )
    @overload
    
    def method_one(self,a,b):
        print(f"This is method with 2 parameters {a} & {b}")   

obj1=Example()
obj1.method_one()
obj1.method_one(2, 4)

'''
class Example:
    
    def __init__(self,*b):  #we can implement constructor overloading by using variable length arguments
        print(b)
        
    def method_one(self,*a):  #we can implement method overloading by using variable length arguments
        print(a)
    def method_two(self,a=0,b=0,c=0,d=0): # method overloading using default values
        print(a+b+c+d)
        
obj1=Example(6,8)
obj1.method_one(1,2)
obj1.method_one(3,4,5)        
obj1.method_two()
obj1.method_two(1)
obj1.method_two(3,6)
obj1.method_two(5,7,8)

