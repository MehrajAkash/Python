
def my_function():
    print("HEllo from a function")

my_function()

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil","Refsnes")
# Arbitrary Arguments *
# if the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("Faraz","Akram","Linu")

# Keyword Arguments
def my_function(child3,child2,child1):
    print("The youngest child is " + child3)

my_function(child1="Mehraj",child2="Hossain",child3="Akash")

# Arbitrary keyword Arguments **
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Zakir", lname="Hossain")

# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function()
my_function("Germany")

# Passing list as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple",'banana','cherry']
my_function(fruits)

