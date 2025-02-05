a = 23
b = "123"
c = 1.0
#or 
d, e, f = 12, "12", 1.9


print(d,e,f)
print(a,b,c)

#Checking type of a variable 

print(type(a))
print(type(b))
print(type(c))

#Type conversion 
# int(), str(), flaot()

a = float(a)
b = int(b)
c = str(c)

print(a,b,c)

#Scope of a variable 

globl = 12 #Global variable 
def f():
    a = 12 #local variable
    print(a)

f()