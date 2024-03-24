'''
Palindrome
'''

s=input("enter a string")
a=True
for i in range(len(s)):
    if s[i]!=s[len(s)-1-i]:
        a=False
        break
if a:
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")