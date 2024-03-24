'''

Types of arguments:
 1. Formal Arguments:
     a.defualt arguments
     b.variable length positional arguments
     c.variable length keyword arguments
 2. Actual Arguments:
     a.positional arguments
     b.keyword arguments
     
special cases:
>passing positional arguments and keyword arguments for single function
'''
'''
def add(a,b):  
    print("a:",a)
    print("b:",b) 
    c=a+b
    print("sum:",c)

add(4,2)  #positional arguments
add(b=4,a=2)  #keyword arguments
add(8,b=6)
#add(8,a=6) Type error-add() got multiple values for a
#add(b=6,8) syntax error- positional argument can't be passed after keyword argument
#add(2,3,4) 

def addition(*a):  #variable length positional arguments
    print(a)
    
addition(1,2,3,4,5)
'''
'''
def add(a=0,b=0): #define some default values to arguments
    print("a:",a)
    print("b:",b) 
    c=a+b
    print("sum:",c)
add(2)
'''
'''
'''
def adding(*a):
    b=0
    for i in a:
        b=b+i
    print("sum:",b)
adding(1,2,3,4,5)

def display_details(**a): #variable length keyword arguments
    print(a)
    
display_details(a=1,b=2,c=3,d=4)

def mixed_v_arg(*a,**b):
    print(a,b)
mixed_v_arg(1,2,3,4,c=4,d=5,b=6)
#mixed_v_arg(c=4,d=5,b=6,1,2,3) syntax error- positional arguments can't be passed after keyword arguments

