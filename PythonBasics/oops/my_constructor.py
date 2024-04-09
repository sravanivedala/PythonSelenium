'''
Constructor: is a method used to construct an object

1. Constructor is not mandatory
    eventhough we can't create a constructor python interprets default constructor in backend

2. Constructor will be called implicitly when an object is created

3. Constructor can also be called explicitly whenever we want

4. Constructor can be defined with/without parameters
'''
class HumanBeing():
    def __init__(self): #constructor without parameters
        print("This is a constructor")
    def display_details(self):
        print("This is HumanBeing Method")

sravani=HumanBeing()
sravani.__init__()
sravani.display_details()

print(dir(sravani)) #it displays what are the methods available for the object



