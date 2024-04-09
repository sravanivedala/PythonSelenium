'''
Exception: Something not normal
Exception handling: handling of abnormal/unexpected behaviors.
Types of errors:
    1. Compile time errors: This can't be handled. Developer/coder/programmer is solely responsible for this.
    2. Run-tme errors: These are unexpected and can be handled
    
How to handle exception?
- using single try-single except default block 
- using single try- specific except block
- using single try-multiple specific except blocks
- using single try- multiple specific except and single default except blocks
- nested try-except blocks
- try-except-finally
    finally block contains the independent actions which must be performed after try block whether exception is there or not
'''

print(1+2)  #3
print(5-3)  #2
print(4*6)  #24
'''try:
    print(9/0)
    
except:
    print("9/0 is Zero division error:division by zero")
'''
'''try:
    #print(9/"a")
    #print(9/0)
    a=[1,2,3]
    print(a[4])
    
except ZeroDivisionError:
    print("9/0 is Zero division error:division by zero")'''
    
try:
    try:
        print(9/0)
        #print(9/3)
    except ZeroDivisionError:
        print(9/"a")
            
    
except TypeError:
    print("Type error: unsupported operand type for /: int and string")   

except Exception as e:
    print("Exception thrown at line 25",e)

finally:
    print("This is 'finally' block")
    
'''except: #default except block
    print("Exception thrown at line 25") 
  '''

    
print(2**4)  #16
print(9//4)  #2