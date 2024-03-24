'''
Looping Statements: To execute any code repeatedly

1. While Loop: To execute repeatedly until condition is fulfilled(as long as
                condition is satisfied)
        steps in while loop
        a. Initialization of a conditional variable
        b. Define loop with the condition
        c. Increment/Decrement section

2. For Loop: Executes a code repeatedly based on sequence or range provided.

Loop Control statements:
1.break
2.continue
  
'''
'''
count=1
while count<=5:
    print("Hello world!")
    count=count+1
'''
'''
for count in range(5):
    print("Hello, world!")
'''
'''
for i in "sravani":
    print(i)
'''
'''
count=1
while count<=200:
    if count==100:
        break
    print(count)
    count=count+1
'''
'''
count=1
while count<=200:
    if count==100:
        count=count+1
        continue
    print(count)
    count=count+1
'''
'''
for i in range(1,20, 2):
  
    if i==9:
        break
    print(i)


'''
'''
for i in range(1,20, 2):
    
    if i==9:
        continue
    print(i)
'''
'''
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

'''
'''
for i in range(5):  #row
    for j in range(5-i):  #column
        print("*", end="")
    print()
    
'''
for i in range(5):
    for j in range(i+1):
        for k in range(5-i):
            print(" ",end="")
        print("*", end="")
    print()
