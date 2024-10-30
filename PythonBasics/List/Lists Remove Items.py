

list4 = ['apple','banana','cherry','banana']
list4.remove('banana')
print(list4) # list4 =  ['apple','cherry','banana']

list5 = ['apple','banana','cherry']
list5.pop()
print(list5) # list5 = ['apple','banana']

list5.pop(0) # pop() method removes the specified index
print(list5) # list4 = ['banana']

list6 = ['apple','banana','cherry']
del list6[1] # del keyword also removed the specified index
print(list6) # ['apple','cherry']

# del list6   ** del keyword can delete the list completely
list6.clear()
print(list6)  # output will show empty list []
