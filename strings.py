s = "qwertyuiopqwer"


print(s[1:4])  


print(s[:3])   


print(s[3:])   


print(s[::-1])

s = "hello world"

# Updating by creating a new string
s1 = "H" + s[1:]

s2 = s.replace("world", "guys")
print(s1)
print(s2)