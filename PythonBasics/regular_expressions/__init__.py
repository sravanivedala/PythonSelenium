'''
Regular expressions(RegEx): RegEx is used for validating input
'''
import re
'''
a="vVVvvVvivek"

print(re.search("Vivek",a))
print(re.search("vek",a))
print(re.search("v.",a)) #take v as reference prints next character also
print(re.search(".v",a)) #take v as reference prints previous character also
print(re.search("^v",a)) # will check whether starts with given character
print(re.search("k$",a)) #will check whether it ends with the character
print(re.search("v*",a)) #checks for repetition from zero position
print(re.search("v+",a)) #checks for repetition from 1st position
print(re.search("vV?",a))
'''

a="V95S ravani"
# print(re.search("95{0,3}",a))
print(re.search("\\s",a))
print(re.subn("\\d","*",a,6))
