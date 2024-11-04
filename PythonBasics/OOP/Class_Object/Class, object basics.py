class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#*********************************
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("John",36)       
print(p1.name)
print(p1.age) 
print(p1)

#************************************
class person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"    

p1  = person("John",54)
print("Returning value from __str__() by p1 : ",p1,"\n")

#***********************************
# Object Methods
class person:
    def __init__(hl,name):
        hl.name = name

    def myfunc(hello):
        print("Hello my name is ",hello.name, "\n")

p1 = person("Kyle Anderson")
p1.myfunc()            

# delete object value
del p1.name
del p1


class student:
    pass