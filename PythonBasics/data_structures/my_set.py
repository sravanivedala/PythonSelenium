'''
 Set:
    1. An empty set can't be created
    2. Set is heterogeneous
    3. Set is immutable i.e., we cannot change the values in set once created
    4. Set removes duplicate values
    5. Insertion order is not preserved i.e., values are reordered in ascending order
    6. Accessing each element can't be done by using index
'''
a={}  # this will create an empty dictionary
print("a", type(a)) 
print("a",a)

b={1,2,"sai","sravani", True, 7+9j,3.9}
print("b",b)

c=set(range(2,21,2))
print("c",c)
'''c[5]=9
print(" c after modification",c)
It throws error as set is immutable we can't change the values
'''
d={1,1,3,4,4,5}
print("d", d)
#print(d[0]) we can't access each element through its index
e={2,4,2,3,1,8,5,7,6}
print("e",e)

for i in e:
    print(i)
 


     
