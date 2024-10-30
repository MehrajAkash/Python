#************* list copying ***************
thislist = ['apple','banana','cherry']
mylist = thislist.copy()  # ['apple', 'banana', 'cherry']
print(mylist)

thislist = ['animal',4,'people']
mylist = list(thislist)
print(mylist)

thislist = ['animal',4,'people']
list2 = thislist[:]
print(thislist)



# ********* join two lists ***************
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = list1 + list2  # ['a', 'b', 'c', 1, 2, 3]
print(list3)

list1 = ['e','f','g']
list2 = ['i','j','k']

for x in list2:
    list1.append(x)
print(list1)    # ['e', 'f', 'g', 'i', 'j', 'k']


list1 = ['e','f','g']
mylist = list(list1)  # list copying
mylist.extend(list2)  # list joining
print(mylist)    # ['e', 'f', 'g', 'i', 'j', 'k']
