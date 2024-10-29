
list1 = ['apple','banana']
list1.append("orange")  # add an item to the end of the list
print(list1)  # ['apple', 'banana', 'orange']

list1.insert(0,'kiwi')
print(list1) # ['kiwi', 'apple', 'banana', 'orange']

list2 = ['apple','banana']
list3 = ['jackFruit','mango']
list2.extend(list3)   # list3 = ['apple','banana','jackFruit','mango']
print(list2)

thisList = ['Orange','Kiwi']
thisTuple = ('Palm','strawvery')
thisList.extend(thisTuple) # you can add any iterable object with list
print(thisList)

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

list7 = ['mango','orange']
list7.extend(['kiwi'])
print(list7)