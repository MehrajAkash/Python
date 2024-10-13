#importing the complex math module
import cmath

num = 1 + 2j
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.2f}+{2:0.2f}j' .format(num, num_sqrt.real, num_sqrt.imag))

print('Hello')
print('World')

#square root of a number
num = int(input('Enter a integer number: '))
num_sqrt = num ** 0.5
print('The square root of %d is %0.3f' %(num, num_sqrt))

num1 = input('Enter num1: ')
num2 = input('Enter num2: ')
sum = float(num1) + float(num2)
# printing sum of above 2 numbers
print('The sum of {0} and {1} is {2}'.format(num1, num2,sum))
# printing sum of 2 numbers using another way
print('The sum is %.1f' %(float(input('Enter 1st number: ')) + int(input("Enter 2nd number: "))))

