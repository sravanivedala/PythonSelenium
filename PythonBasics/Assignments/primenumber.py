'''
Prime number
'''
'''
num=int(input("Please enter a number"))
a=False
if num==1:
    print(num, "is a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            a=True
            break
if a:
    print(num," is not a prime number")
else:
    print(num,"is a prime number")

'''
a=int(input("Please enter a number"))
if a==1:
    print("It's a Prime number")
for i in range(2,a+1):
    b=a%i
    if b==0 and i<a:
        print("Not a prime number")
        break
    if b==0 and i==a:
        print("It's a prime number")
    
        

