# factorial of a number
num = int(input('Enter number for factorial: '))
fact = 1

if num == 0:
    print('factorial of ', num, ' is: ', fact)
else:
    for i in range(1,num+1):
        fact *= i
    print('factorial of ',num,' is: ',fact)


# Python program to display all the prime numbers within an interval
lower = int(input('Enter a lower value: '))
upper = int(input('Enter upper value: '))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break

       else:
           print(num)