
class A:
    def displayA(self):
        print('In Class A')

class B(A):
    def displayB(self):
        print('In class B')

class C(B): 
    def displayC(self):
        super().displayA()
        super().displayB()
        print("In Class C")        

c = C()
c.displayC()


print()
print('Multiple Inheritance')
class D:
    def display(self):
        print('In D class')
class E: 
    def display(self):
        print("In E class")   
class F(E,D):
    pass

f = F()
f.display()

