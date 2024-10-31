
list1 = ['apple','banana','cherry']
for x in list1: 
    print(x)

print()

for i in range(len(list1)):  # range value starts from 0 automatically
    print(list1[i])

print()

i = 0
while i < len(list1):
    print(list1[i])    
    i = i + 1

print()
# Short hand for loop that will print all items in a list
list2 = ['apple','banana','cherry']

[print(x) for x in list2]
