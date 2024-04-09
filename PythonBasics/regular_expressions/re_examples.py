import re
'''
1. Mobile number validation    
  - should have 10 digits
  - first digit should be any digit from 5-9
  - remaining digits can be any digit from 0-9
my_re="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
my_re="[5-9][0-9]{9}"
my_re="[5-9]\\d{9}"
'''

number=input("Please enter a mobile number:")
#my_re="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
my_re="[5-9][0-9]{9}"
print(re.fullmatch(my_re,number))
      

match_object=re.fullmatch(my_re,number)

if match_object!=None:
    print("You have entered a valid phone number")
    
else:
    print("You have entered an invalid phone number")
