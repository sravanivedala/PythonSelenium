'''
Method= every function defined inside a class

self keyword refers to the object we have created
'''

'''defining a class'''
class HumanBeing():
    def __init__(self,name,color,height,gender): #constructor with parameters
        self.name=name
        self.color=color
        self.height=height
        self.gender=gender
        
    def display_details(self):  
        print(f"{self.name} am a human being in {self.color} color, {self.height} feet height, {self.gender} gender") 
        
vivek=HumanBeing("Vivek","Black",5.3,"Male")    # Instantiation: created an object which belongs to HumanBeing class
vivek.display_details()  # I called a method from HumanBeing class using vivek object
#print(type(vivek))

sravani=HumanBeing("Sravani","White",5.4,"female")
sravani.display_details()