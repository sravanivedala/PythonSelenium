'''
Conditional statements:

1. if statement
2. if-else statement
3. series if-else statements
4. Nested if-else statements

Logical operators in conditional statements
'''

age=int(input("please enter your age:"))
'''
if age>=13:
    print("Allow inside")
else:
    print("push them out")
print("program stopped")
'''
'''
if age>18:
    print("You are an adult")
elif age >=13:
    print("You are a teenager")
else:
    print("You are a child")
    '''
'''
if age>13:
    if age>18:
        print("You are an adult")
    else:
        print("You are a teenager")
        
else:
    print("You are a child")
    '''
if age>=13 and age<=18:
    print("You are a teenager")
else:
    print("You are not a teenager")