'''

  List:
  
  1. We can create an empty list
  2. List is heterogeneous
  3. Accessing:
     a. By using Index
     b. Slicing operator
     c. By using Loops
     
     Index: Position value of any element present in the list
      from left to right --> 0,1,2,3....
      from right to left --> -1,-2,-3,....
      
      syntax: list_name[]  --> common for all data structures
  4. List is mutable i.e., list can be modified once created
  5. List stores duplicate values
  6. Insertion order is preserved i.e., list stores the values as it is, it will not reorder the values

'''
'''
a=[] # 1. We can create an empty list
print("a", type(a))
print("a",a)

b=[1,2,3,"Bhanu","sravani",3.5,3+5j,True]  # 2. List is heterogeneous
print("b",b)

c=list(range(6))
print("c", c)

d=list(range(2,21,2))
#print("d", d)
#print(d[4])
#print(d[-4])

print(" d list before modifying",d)
d[5]=11
print(" d list after modifying",d)

e=[1,2,3,3,5,5,6]
print("e",e)

f=[5,7,4,9,5,2,3,6]
print("f",f)
print("====f list elements using for loop====")
for i in f:
    print(i)
    
print("====d list elements using while loop====")
i=0

while(i<len(d)):
    print(d[i])
    i=i+1
'''
'''
c=list(range(2,21,2))
print("c",c)
d=[1,2,3,4]
print(d)
c.append(56)
print("c after appending 56",c)
c.append(d)
print("c after appending d",c)
c.extend(d)
print("c after extending d",c)
#c.clear()
#print(c)
e=c.copy()
print("e",e)

print(c.index(4))
print(c.index(4,11))
c.insert(9,90)
print(c)
print(c.pop(8))
print(c)
print(c.pop())
print(c)

c.remove(56)
print(c)

c.reverse()
print(c)

c.pop(3)
print(c)

c.sort()
print(c)

print(c.count(2))

print(len(c))
'''
'''
a=[2,5,5,3,7,5,3,8,10,2,7,5,3]
for i in range(len(a)):
    for j in range(i+1):
        if a[j]==a[i]:
            break
    print(a[i], "comes", a.count(a[i]) )
'''
