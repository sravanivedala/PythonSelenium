'''
Created on 23-Mar-2024

@author: Rakesh
'''
'''
a=[2,5,5,3,7,5,3,8,10,2,7,5,3]
b=a.copy()
for i in b:
    ele_count=b.count(i)
    print(f"{i}---> {ele_count} times")
    for j in range(ele_count):
        b.remove(i)
print(a)
'''
'''
a=[1,3,4,5,5,3,4,5,3]
b=a.copy()
for i in b:
    ele_count=b.count(i)
    print(f"{i}---> {ele_count} times")
    for j in range(ele_count):
        b.remove(i)
print(a)
'''
a=[1,3,4,5,5,3,4,5,3]
b=a.copy()
i=0
while True:
    element=b[i]
    ele_count=b.count(element)
    print(f"{element}---> {ele_count} times")
    for j in range(ele_count):
        b.remove(element)
    if len(b)==0:
        break
    
print(a)