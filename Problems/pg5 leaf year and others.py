print(pow(2,3))

a = 1
while a<=3:
    year = int(input('Enter a year: '))

    if(year % 400 == 0) and (year % 100 == 0):
        print('{0} is a leap year' .format(year))
    elif(year % 4==0) and (year % 100 != 0):
        print('%d is a leap year' %year)
    else:
        print('{0:.2f} is not leaf year' .format(year))
    a+=1

print('')

# detemine prime number
for j in range(1, 5):

    num = abs(int(input('Enter a number: ')))
    result = False

    if num == 0 or num == 1:
        print(num,' is not a prime number.')

    elif num > 1:
        for i in range(2, num):    # in range value of num = num-1
            if (num % i) == 0:
                result = True
                break

    if result:
        print(num,' is not a prime number')
    else:
        print('prime number',num)