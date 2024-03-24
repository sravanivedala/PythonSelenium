'''
Operators: Symbols which performs operations on one or more operands(Variables)
1.Arithmetic operators: +,-,*,/,%,**(exponent), //(Integer Division) numerical datatypes
2.Logical operators: AND,OR, NOT  boolean datatypes
3.Assignment operators: =
4.Comparison/Relational operators: >,<,>=,<=,==,!= (input numeric,output boolean)
5.a.Increment operator: +=
5.b.Decrement operator: -=
6.Membership operators: in, not in (object is in group)
7.Identity operators: is, is not  (whether two objects identical or not)
'''
'''
a=5
b=3
c=a+b
x=a/b  #it gives quotient as decimal
y=a%b  #it gives the remainder
z=a//b #it gives the quotient as integer 

print("c",c)
print("x",x)
print("y",y)
print("z",z)'''
#d=input("please enter value for d:")  it is taking input as string we need to change the type'''
''''d=int(input("please enter value for d:"))  # type-casting
e=int(input("please enter value for e:"))
f=d+e
print("f=", f)
print(type(d))
print(type(e))
print(type(f))
'''
'''
#Logical operators

print(True and True)
print(True and False)
print(False and False)

print(True or False)
print(True or True)
print(False or False)

print(not True)
print(not False)

'''
'''
# Relational operators
print(5>8)  #False
print(5>=8)  #False
print(5<8)  #True
print(5<=8)  #True
print(5==8)  #False
print(5!=8)   #True

'''
'''
#Increment/Decrement operators

a=3
a=a+1
a+=1
a-=1
print(a)
'''
'''
# Membership operators
print('a' in 'sumanth')
print('A' in 'sumanth')
print('A' not in 'sumanth')
'''

a=2
b=2.0
print(a==b)  # value only checked here
print(a is b) #value and datatype must be checked here 
print(id(a))
print(id(b))

x= 2
y= 2
print(x is y)
print(id(x))
print(id(y))



