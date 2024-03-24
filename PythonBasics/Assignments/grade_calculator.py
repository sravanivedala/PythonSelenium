'''
Grade Calculator
'''
score=int(input("please enter the score value"))
if score>=90 and score<=100:
    print("Grade is A")
elif score>=80 and score<90:
    print("Grade is B")
elif score>=70 and score<80:
    print("Grade is C")
elif score>=60 and score<70:
    print("Grade is D")
elif score>=50 and score<60:
    print("Grade is E")
else:
    print("Grade is F")