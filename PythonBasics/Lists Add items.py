
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


list7 = ['mango','orange']
list7.extend(['kiwi'])
print(list7)