'''
Constructor Inheritance:
 
1.Parent class constructor will be inherited and called implicitly when child class object is created(when no constructor is therein child class)
    

'''
class GrandFather:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("This is Grandfather constructor")
        
    def gf_method(self):
        print(f" Grandfather's name is {self.name} and {self.age} years old")
        
class Father(GrandFather):
    def __init__(self,name,age,aadhar_id):
        #self.name=name
        #self.age=age
        self.aadhar_id=aadhar_id
        print("This is Father constructor")
        GrandFather.__init__(self,name,age)
        #super().__init__(name,age)
        
    def f_method(self):
        print(f"Father's name is {self.name} , {self.age} years old and has aadhar-id {self.aadhar_id}")
        
    def car(self):
        print("This is father's car")
        
print("====GrandFather====")        
ajja=GrandFather("ajja",85)
ajja.gf_method()
print("====Father====")
appa=Father("appa",58,1)
appa.f_method()


