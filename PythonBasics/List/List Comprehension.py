
fruits = ['apple','banana','cherry','kiwi','mango']
newlist = []

# starts here
for x in fruits:
    if 'a' in x:
        newlist.append(x)
# ends here
print(f"\n newlist: {newlist} \n")  #  newlist: ['apple', 'banana', 'mango']



# with list comprehension you can do all that with only one line of code
newlist2 = [x for x in fruits if "a" in x]
print('newlist2 comprehension: {0} \n' .format(newlist2)) # newlist: ['apple', 'banana', 'mango']


newlist3 = ['apple','banana','Cherry']
newlist4 = [x for x in newlist3 if x != "apple"]

print(f"newlist4 = {newlist4} \n")  # newlist4 = ['banana', 'Cherry']

list5 = [x for x in newlist3]
print(list5)  # list5 = ['apple','banana','Cherry']

list6 = [x for x in range(5)]
print(list6)  # list6 = [0, 1, 2, 3, 4]

list7 = [x for x in range(4,10) if x < 8]
print(list7)   # [4, 5, 6, 7]

#fruits = ['apple','banana','cherry','kiwi','mango']

list8 = [x.upper() for x in fruits]
print(list8)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruit2 = ['apple','banana','cherry']
list9 = ['Hello' for xy in fruit2]
print(list9)  # ['Hello', 'Hello', 'Hello']

# return 'orange' instead of 'banana'
list10 = [x  if x != "banana" else "ORAnge"  for x in fruit2]
print('last line: ', list10)