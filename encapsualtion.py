
class car:
    def __init__(self,year,model,age):
        self.year = year
        self._model = model
        self.__age = age

    def details(self):
        return f"{self.year}, {self._model}, {self.__age}"
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            age = self.__age
        else:
            print("Invalid age")



vehicle = car(2024,"ERC",1)

print(vehicle.year)
print(vehicle._model)

#print(vehicle.__age) Not allowed in this way since its a private variable
print(vehicle.get_age())    #Accesing it using its own method

vehicle.set_age(2)
print(vehicle.details())