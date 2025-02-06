#Numeric data types in python


a = 12
b = 12.1
c = 12 + 12j    # real + imaginary
d = complex(2,4)    #(real, imaginary)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(c)
print(c.real,c.imag) #Printing real and imaginary numbers
#Operations in complex numbers
print(c - d)
print(c * d)