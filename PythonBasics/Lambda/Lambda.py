# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

x = lambda a,b,c : a + b + c
print(x(2,4,6))

# the power of lambda is better shown when you use them as an anonymous function inside another function
def myfunc(n):
    return lambda a : a * n
        # n=2  a=11
mydoubler = myfunc(2)
print(mydoubler(11))



def myfunc(n):
    return lambda m : m * n

mytripler = myfunc(3)
myhalfer = myfunc(0.5)

print(mytripler(12))
print(myhalfer(12))
