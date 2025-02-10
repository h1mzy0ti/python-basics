# List implementation
# In-built dynamic sized array and can store any sort of items including another list

# List of numbers
list = [1,2,3,4,5]
# List of strings
list1 = ["Dog", "Cat", "Bird"]
# Mix list 
list2 = [1,"Goat",3.2,True]

print(list,list1,list2, sep="\n")

# Repeated Elements
a = [3] * 3
b = ["Cat"] * 3
print(a,b,sep="\n")
print(a[1],a[-1],sep=" | ")

# Inserting - append = insert at the end, extend = insert multiple at the end, insert = insert at any position
empty_list = []
empty_list.append("Hello")
empty_list.extend(["World", "I am Hari"])
empty_list.insert(3,",Bye")
print(empty_list)