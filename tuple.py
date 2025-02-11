# Initialization
tup1 = (1,2,3,4)
tup2 = ("Dog","Cat")
tup3 = (92.0,8.0,9.0)
print(tup1,tup2,tup3)

# Accessing
print(tup1[0])
print(tup2[1:])
print(tup3[:1])

a, b = tup2
print(a,b,sep=" ")

#deleting
#del tup1
#print(tup1)

#built in func index and count
print(tup2.index("Dog"))
print(tup3.index(9.0))