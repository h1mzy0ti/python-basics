#Class and object
class car: 
    brand = "Mercedes"          # Class attribute / variable

    def __init__(self,model,year):
        self.model = model      # Instance attribute / variable
        self.year = year        # Instance attribute / variable

vehicle = car("GlS 450",2023)
print(vehicle.model,vehicle.year, sep=" & ")
print(car.brand)