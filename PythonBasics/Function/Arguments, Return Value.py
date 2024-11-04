
def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(8))

def function2():
    pass

# Positional Only Arguments
def my_function(x,/):
    print(x)
# my_function(x=44)  ,/ you will get an error if you try to send a keyword argument    
my_function(5)    


def my_function(x,y):
    print(x,y)

my_function(x=11,y=25) 

# Keyword-Only Arguments 
def my_function(*, x):
    print(x)
# my_function(44)  You will get an error if you try to send a positional argument.
my_function(x=44)

# Combine Positional-Only and Keyword-Only
def my_function(b,/ , *,c):
    print(b, c)

my_function(66,c=77)

