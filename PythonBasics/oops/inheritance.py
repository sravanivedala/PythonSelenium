'''
Inheritance: Using the properties/characteristics (variables or methods) of one class(parent class) in other class(sub classes)
    1. Single level Inheritance (GrandFather --> Father)
    2. Multilevel Inheritance (GrandFather --> Father --> Child)
    3. Multiple Inheritance (Father,Mother --> Child)
    
Method resolution order(MRO): whenever methods of same name available in child class and parent classes, it will check first in child class 
                                then parent classes in the order which we have given

'''
class GrandFather:
    def gf_method(self):
        print("This is Grandfather method")
        
    def car(self):
        print("This is Grandfather's car")
      
class Father(GrandFather):
    def f_method(self):
        print("This is Father method")
    def car(self):
        print("This is father's car")
        GrandFather.car(self)

class Mother:
    
    def m_method(self):
        print("This is Mother method")
        
    def car(self):
        print("This is mother's car")         
          
class Child(Father, Mother):
    
    def c_method(self):
        print("This is child method")
    def car(self):
        print("This is my car") 
        Father.car(self)
        Mother.car(self)
        #GrandFather.car(self)
ajja=GrandFather()
appa=Father()
print("====GrandFather====")
ajja.gf_method()
print("====Father====")
appa.f_method()
appa.gf_method()       

myself=Child()
print("====Child====")
myself.c_method()
myself.f_method()
myself.gf_method()
myself.m_method()
myself.car()

print("====MRO====")
print(Child.mro())