import random

a = 5
b = 10

temp = a
a = b
b = temp

print('Value of a after swapping a: {0}'.format(a))
print('Value of b after swapping b: {}'.format(b))

# Simple swapping
a = 50
b = 100

a,b = b,a
print('a = ',a)
print('b = ',b)

# Kilometers to Meter
kilometers = float(input("Enter value in kilometers: "))
miles = kilometers * 0.621371
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles))

c=1
while c<=5:
    b = (random.randrange(1,9)) # random.randint(a,b)
    a = int(input('Enter a random number which is between 1 and 9: '))
    if a==b:
        print('You have won the match')
    else:
        print('You Have lost')
        print('Random number was: ',b)
    c+=1
