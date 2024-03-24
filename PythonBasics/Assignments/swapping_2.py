'''
Swapping the values of two variables without using a third variable
'''
a=int(input("please enter value for a:"))
b=int(input("please enter value for b:"))
a=a+b
b=a-b
a=a-b
print("After swapping")
print("a=",a)
print("b=",b)