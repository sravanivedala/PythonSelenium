'''
Leap Year 
'''
year=int(input("Please enter a year"))
'''if year%100==0 and year%400==0:
        print(year, "is a leap year")
elif year%4==0 and year%100!=0:
        print(year, "is  a leap year")
else:
    print(year, "is not a leap year")'''
    
if year%100==0:
    if year%400==0:
        print(year, "is  a leap year")
    else:
        print(year, "is not a leap year")
else:
    if year%4==0:
        print(year, "is  a leap year")
    else:
        print(year, "is not a leap year") 