"""
b = 1
 while b <= 3:
     n = int(input('Enter a positive number: '))
     if n % 2==0:
         print("%d is even" %n)
     else:
         print('{0} is odd'.format(n))
     b+=1

"""


d = -55
print(abs(d)) #absolute value

n=0
while n <= 3:
    number = abs(int(input('Enter a positive number: ')))

    if number%2==0:
        print('%d Even number' %number)
    else:
        print('{} Odd number' .format(number))
    n+=1
print('1st part end')
print('')

a = 1
while a<=5:
    num = float(input("Enter a number: "))
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print('Negative number')
    a+=1



