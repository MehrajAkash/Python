#from itertools import count

ns = int(input('Enter a number for nth series sum: '))
num = ns
sum = 0
while(ns > 0):
    sum += ns
    ns -= 1
print('Sum of',num,'th series: ',sum)



nterms = int(input("Enter a number: "))
n1,n2 = 0,1
count = 1

if nterms <= 0:
    print('Please Enter a positive integer: ')
elif nterms == 1:
    print('Fibonacci series upto ',nterms,": ")
    print(n1)
else:
    print('Fibonacci Sequence: ')
    while count <= nterms:
        print(n1)
        n = n1
        n1 = n2
        n2 = n+n1

        count += 1


