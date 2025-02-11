# List implementation
# In-built dynamic sized array and can store any sort of items including another list

# List of numbers
list0 = [1,2,3,4,5]
# List of strings
list1 = ["Dog", "Cat", "Bird"]
# Mix list 
list2 = [1,"Goat",3.2,True]

print(list0,list1,list2, sep="\n")

# Repeated Elements
a = [3] * 3
b = ["Cat"] * 3
print(a,b,sep="\n")
print(a[1],a[-1],sep=" | ")

# Inserting - append = insert at the end, extend = insert multiple at the end, insert = insert at any position
el_list = []
el_list.append("Hello")
el_list.extend(["World", "I am Hari"])
el_list.insert(3,",Bye")
print(el_list)
el_list[0] = "Hi"
print(el_list)
# Removing elements - remove -remove elements form the first occurance, pop- remove elements at a positon, del - at position
el_list2 = [1,2,3,4,5,6,7,8,8]
el_list2.remove(2)
print(el_list2)
el_list2.pop(0)
print(el_list2)
del el_list2[-1]
print(el_list2)


