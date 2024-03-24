'''
Fibonacci Series
'''
n=int(input("please enter number of terms"))
num1=0
num2=1
count=1
print(num1)
print(num2)
while(count<n):
    num3=num1+num2
    count=count+1
    print(num3)
    num1=num2
    num2=num3
