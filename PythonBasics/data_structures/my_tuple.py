'''
Tuple:

 1. We can create an empty tuple
 2. Tuple is heterogeneous
 3. Tuple is immutable i.e., we cannot change the values in tuple once created
 4. Tuple stores duplicate values
 5. Insertion order is preserved 
 6. Accessing each element can be done by using index

'''
a=()
print("a",type(a))
print("a",a)

b=(1,3,"Sravani", 4.7,False,5+8j)
print("b",b)

c=tuple(range(1,20,2))
print("c ",c)
'''
c[5]=12
print("c after modifying",c) 
It throws error as tuple is immutable we can't change the values
'''
d=(1,2,2,3,4,4)
print("d",d)
print(d[-1])
e=(2,1,5,9,3,7,8,2)
print("e",e)
print("====e tuple elements using for loop====")
for i in e:
    print(i)
print("====c list elements using while loop====")
i=0
while(i<len(c)):
    print(c[i])
    i=i+1

