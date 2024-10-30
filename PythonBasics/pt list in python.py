
n = input("enter a text of numbers: ")
listnum = n.split()
sum = 0

print('list: ',listnum)
for num in listnum:
    sum = sum + int(num)

print("Sum of numbers : ",sum)    


numwords = 0
numletters = 0
numdigits = 0
text = input('Enter a text: ')
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numletters += 1
    elif x >= '0' and x <='9':
        numdigits += 1
    elif x == ' ':
        numwords += 1

print(numletters)        
print(numdigits)
print(numwords+1)

    
