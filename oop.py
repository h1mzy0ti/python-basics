#Class and object
class car:
    brand = "Mercedes"

    def __init__(self,model,year):
        self.model = model
        self.year = year

vehicle = car("GlS 450",2023)
print(vehicle.model,vehicle.year, sep=" & ")