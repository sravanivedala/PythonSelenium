'''
Types of Variables:
1. Instance/Object variables: values changes from object to object
2. Static/class Variables : same value throughout the class
3. Method/Local Variables : used only for that particular method

Note:
1. Instance variables can be declared anywhere with the help of self keyword.
2. Static variables can be declared anywhere with the help of class name

'''

class Student():
    #school_name="iQuest" # Static/ class Variable
    def __init__(self,name,roll_no):
        self.name=name # Instance variables
        self.roll_no=roll_no
        Student.school_name="iQuest" # Static/ class Variable
    def display_details(self):
        print(f"{self.name} has {self.roll_no} roll no. from {Student.school_name}")
        
    def display_score(self, english, science, maths):  
        self.english=english  #converting local variable into instance variable to use that variable in any other method
        total=english+science+maths  # method/local variables
        print(f"{self.name} has scored {total}")
    