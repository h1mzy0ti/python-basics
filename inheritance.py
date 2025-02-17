# Inheritance - Single, Multiple, Multilevel, Hierarchical, Hybrid
# Single
class car:
    def __init__(self,year,model):
        self.year = year
        self.model = model
    def display(self): 
        print(self.year,self.model, sep = " & ",end=" --> ")

class suv(car):
    def technology(self):
        print("AWD / 2WD")

# Multi-level (at this point)
class hummer(suv):
    def features(self):
        print(f"{self.year}  is {self.model} has this features ...")


#Multiple
class compact():
    def is_compact(self):
        print("This is a compact car")

class creata(car,compact):
    def manufacturer(self):
        print("Hyundai")


# Code for single level
car1 = suv(2023,"Thar")
car1.display()
car1.technology()

#Code for multi-level
car2 = hummer(2024,"EV")
car2.technology()
car2.display()

#Code for multiple 
car3 = creata(2024,"EX")
car3.manufacturer()
car3.display()