#Basic function
def bFunc(val):
    print(val)

def rFunc(val):
    print(val)
    rFunc(val)

bFunc(1) 
#rFunc(1) #This will cause error because by default python allows 1000 times recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))  
