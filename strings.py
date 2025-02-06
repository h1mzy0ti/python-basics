s = "Welcome to the world"
multi_line = """ Apple is a fruit,
Banana is a fruit, Tomato is a vegetable.
"""
print(s)
print(multi_line)
print(type(s))

#Can be accesed like an array
print(s[0])
print(s[-1])

t = s + s[0]                        # Updating in strigs
h = s[0] + s[0]                     # Combining two string char of the string
r = "w" + s[1:]                     # Updating by position not index
y = s.replace("Welcome", "Hello")   # replace the woprd Welcome with Hello
print(t)
print(h)
print(r)

#Slicing strings
print(s[1:4])                       # will start from index 1 to 3 as elc
print(s[:4])                        # will start from index 0 to 3 as welc
print(s[5:])                        # will sttart from index 5 to end
print(s[::-1])                      # Reverse the string
print(s[:-1])                       # will start from index 0 and end in index -1 which is the indexing from teh end

#String methods - 
s = "unformated text"
print(s)
print(s.title())                    # Capitalize the first letter of each word
print(s.capitalize())               # Capitalize the first letter of the string
print(s.swapcase())                 # Swap the case of the string