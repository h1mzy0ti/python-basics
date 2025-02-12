# Normal Function

def normal_function(value,info):
    print(f"The value is -  {value} and the info is - {info} ")

normal_function(1,"Normal function")

#using self (Refers objects )
class self_function:
    def __init__(self,value,info):
        self.value = value
        self.info = info
    
    def prind(self):
        print(f"The value is {self.value} and info is {self.info}")


func = self_function(12,"Hello")
func.prind()

#*args (Non keyword variable lenght argument) basically a tuple
class ar:                   # With class
    def funn(*args):
        a = args + args
        print (a)

ar.funn("Hello")

def fun(*numbers):
        step = list(map(int,numbers))
        for i in step:
            i *= 2
            print(i)

fun(12,23,23)

#**kwargs (keywords variable length argument) basically a dictionary

def karg(**val):
    print(val)
karg(name = "Bob", age = 12)
#karg(1 = "Apple", 2 = "Samsung") # no strings

class kargt:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        print(kwargs)

    def check(self,val):
        for i in self.kwargs.keys():
            if i == val:
                print(True)
            


obj = kargt(value = "Placeholder", info = "This is a testing")
obj.check("info")