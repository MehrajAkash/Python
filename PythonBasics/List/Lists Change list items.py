
thislist = ['apple','banana','JackFruit','kiwi','watermelon']
thislist[0] = 'blackcurrant'
print(thislist)

thislist[1:3] = ['nut','coconut']
print(thislist)

list2 = ['apple','cherry','orange']
list2[1:2] = ['mango','lichi']  # cherry replaced by mango and lichi
print(list2)

list3 = ['apple','cherry','orange']
list3[0:2] = ['Dragon']
print(list3)

list4 = ['apple','banana','cherry']
list4.insert(2,"watermelon")
print(list4) # ['apple', 'banana', 'watermelon', 'cherry']