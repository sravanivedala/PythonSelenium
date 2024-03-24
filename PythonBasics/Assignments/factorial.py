'''
Factorial
'''
i=int(input("please enter a number"))
fact=1
for i in range(1,i+1):
    fact=fact*i
print("Factorial of ", i ,"is", fact)