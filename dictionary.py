

d1 = {1:"Dog",2:"Cat",3:"Mouse"}          #using {}
d2 = dict(a = "Car",b = "Bus",c ="Truck") #using dict() constructor
print(d1)
print(d2)

#Accessing
print(d1[1])        #using key
print(d1.get(1))    #using get() method

#Adding and updating
d1[4] = "Pig"       #Adding
d1[1] = "Sheep"     #Updating

print(d1,d2,sep ="\n")

# Misc
x = d2.keys()       #Fetching keys
y = d2.values()     #Fetching values
print(x,y,sep="\n")

#Removing
del d1[1]
d2.pop("a")     #Removing with key
d2.popitem()    #Remove the last item
print(d2)
#d1.clear()     #Wipe out he entire dictionary

#Detecting a value or key if it exist in the  dict by iterating 
di = dict(a = "Gaming",b = "Finance",c = "Politics",d = "Geography")


if "Politics" in di.values() and "a" in di.keys():
    print(True)
else:
    print(False)